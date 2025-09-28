"""
Actividad Formativa 2 — Simulación y análisis de señales con la Transformada de Fourier (Python)
Autor: Abraham Rubén Tamez Rodríguez
Requisitos: numpy, matplotlib
Uso: python fourier_analysis.py
"""
import os, json
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Funciones auxiliares
# -------------------------------

#Función escalón unitario: devuelve 0 si x<0, 1 si x>=0

def heaviside(x):
    return (x >= 0).astype(float)

#Para generar un pulso rectangular centrado en 'center'
#    - width: duración del pulso
#    - amp: amplitud del pulso 

def make_rect_pulse(t, width=0.2, center=0.0, amp=1.0):
    return amp * ((t >= center - width/2) & (t <= center + width/2)).astype(float)


# Calcular la Transformada de Fourier de las señales generadas 
#  
#    Calcula la FFT y reordena frecuencias con fftshift
#    - x: señal en el tiempo
#    - fs: frecuencia de muestreo
#    Devuelve:
#      f: eje de frecuencias (sin ordenar)
#      X: FFT original
#      fs_axis: eje de frecuencias ordenado
#      Xs: FFT desplazada (centrada en 0 Hz) 

def compute_fft(x, fs):
    N = len(x)
    X = np.fft.fft(x)
    f = np.fft.fftfreq(N, d=1/fs)
    Xs = np.fft.fftshift(X)
    fs_axis = np.fft.fftshift(f)
    return f, X, fs_axis, Xs


#Genera y guarda una gráfica simple en PNG 

def save_plot(path, x, y, xlabel, ylabel, title):
    plt.figure()
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(path, dpi=160)
    plt.close()

# -------------------------------
# Programa principal
# -------------------------------

# Carpeta de salida para las gráficas 
def main():
    base = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(base, "outputs")
    os.makedirs(out, exist_ok=True)


# Parámetros de muestreo, aqui puedes ajustar para ver diferentes resutlados
    fs = 2000.0 # frecuencia de muestreo en Hz
    T = 1.0 # duración de la señal en segundos
    N = int(T*fs) # número total de muestras
    t = np.arange(N)/fs - T/2 # vector de tiempo centrado en 0


    # -------------------------------
    # 1. Generación de señales
    # -------------------------------

    rect_width = 0.2
    x_rect = make_rect_pulse(t, width=rect_width, center=0.0, amp=1.0) # pulso rectangular
    x_step = heaviside(t) # escalón unitario
    f0 = 50.0 
    x_sin = np.sin(2*np.pi*f0*t)  # seno de 50 Hz el que se puso en linea 86


# -------------------------------
# 2. FFT y espectros
# -------------------------------
# Función auxiliar: calcula FFT de 'x' con 'fs' y guarda:
#  - Espectro de magnitud |X(f)| en {prefix}_mag.png
#  - Espectro de fase ∠X(f) en {prefix}_fase.png


    def plot_fft(x, prefix):
        f, X, fs_axis, Xs = compute_fft(x, fs) # FFT y ejes reordenados (0 Hz al centro)
        mag = np.abs(Xs) # magnitud del espectro
        phase = np.angle(Xs) # fase del espectro
        # Guardar gráficos
        save_plot(os.path.join(out, f"{prefix}_mag.png"), fs_axis, mag, "Frecuencia (Hz)", "|X(f)|", f"Espectro de magnitud: {prefix}")
        save_plot(os.path.join(out, f"{prefix}_fase.png"), fs_axis, phase, "Frecuencia (Hz)", "Fase (rad)", f"Espectro de fase: {prefix}")

    # Guardar gráficos de tiempo
    save_plot(os.path.join(out, "01_rect_tiempo.png"), t, x_rect, "Tiempo (s)", "Amplitud", "Pulso rectangular")
    save_plot(os.path.join(out, "02_step_tiempo.png"), t, x_step, "Tiempo (s)", "Amplitud", "Función escalón unitario")
    save_plot(os.path.join(out, "03_seno_tiempo.png"), t, x_sin,  "Tiempo (s)", "Amplitud", "Señal senoidal 50 Hz")

    # FFT y espectros
    plot_fft(x_rect, "04_rect")
    plot_fft(x_step, "05_step")
    plot_fft(x_sin,  "06_seno")

# -------------------------------
# 3. Propiedades de la Transformada de Fourier
# -------------------------------
# a) Linealidad:
#    F{a·x1(t) + b·x2(t)} = a·X1(f) + b·X2(f)
#    Verificamos comparando la FFT de la combinación en tiempo contra la combinación lineal de las FFT individuales.
    a, b = 1.5, -0.7 # coeficientes arbitrarios
    x1, x2 = x_sin, x_rect # señales a combinar
    x_lin = a*x1 + b*x2 # combinación lineal en tiempo
    
    # FFTs
    f, X1, _, X1s = compute_fft(x1, fs)
    _, X2, _, X2s = compute_fft(x2, fs)
    _, XL, fs_axis, XLs = compute_fft(x_lin, fs)
    rhs = a*X1s + b*X2s # combinación lineal en frecuencia
    lin_error = float(np.max(np.abs(XLs - rhs))) # error máximo entre ambos lados

    save_plot(os.path.join(out, "07_linealidad_tiempo.png"), t, x_lin, "Tiempo (s)", "Amplitud", "Linealidad: a·seno + b·pulso")
    save_plot(os.path.join(out, "08_linealidad_mag.png"), fs_axis, np.abs(XLs), "Frecuencia (Hz)", "|X_L(f)|", "Linealidad: |FFT{a·x1+b·x2}|")

# b) Desplazamiento en el tiempo:
#    x(t - t0)  <->  X(f) · e^{-j 2π f t0}
#    Cambia la fase linealmente con f; la magnitud se conserva.
    t0 = 0.05
    
    x_shift = np.interp(t, t - t0, x_sin, left=0.0, right=0.0) # seno desplazado en el tiempo
    # FFT del original vs. desplazado
    _, Xsin, _, Xsins = compute_fft(x_sin, fs)
    _, Xshift, fs_axis, Xshifts = compute_fft(x_shift, fs)
    # FFT teórica del desplazamiento
    phase_factor = np.exp(-1j*2*np.pi*fs_axis*t0)
    X_pred = Xsins * phase_factor
    # Error numérico de verificación
    shift_error = float(np.max(np.abs(Xshifts - X_pred)))

    save_plot(os.path.join(out, "09_desplazamiento_tiempo.png"), t, x_shift, "Tiempo (s)", "Amplitud", "Seno desplazado en el tiempo (t0=50 ms)")
    save_plot(os.path.join(out, "10_desplazamiento_fase.png"), fs_axis, np.angle(Xshifts), "Frecuencia (Hz)", "Fase (rad)", "Desplazamiento: fase de FFT{x(t-t0)}")

    # Escalamiento temporal
    #    x(a·t)  <->  (1/|a|) · X(f/a)
    #    Comprimir en el tiempo ensancha el espectro y reduce su amplitud (1/|a|).
    a_scale = 2.0
    x_scaled = np.interp(a_scale*t, t, x_sin, left=0.0, right=0.0)
    _, Xscaled, fs_axis, Xscaleds = compute_fft(x_scaled, fs)

    # Predicción teórica aproximada: (1/|a|) X(f/a) interpolando real + imag
    from numpy import interp # para interpolación lineal
    Xsin_real = np.real(Xsins)
    Xsin_imag = np.imag(Xsins)
    target_freqs = fs_axis / a_scale
    Xteo_real = interp(target_freqs, fs_axis, Xsin_real, left=0.0, right=0.0) / abs(a_scale)
    Xteo_imag = interp(target_freqs, fs_axis, Xsin_imag, left=0.0, right=0.0) / abs(a_scale)
    X_teo = Xteo_real + 1j*Xteo_imag
    # Error de verificación del escalamiento
    scale_error = float(np.max(np.abs(Xscaleds - X_teo)))

    # Guardar resumen de resultados en JSON
    results = {
        "linearity_max_error_fft": lin_error,
        "time_shift_max_error_fft": shift_error,
        "time_scaling_max_error_fft": scale_error,
        "sampling_rate_Hz": fs,
        "N_samples": N,
        "duration_s": T,
        "rect_width_s": rect_width,
        "sine_freq_Hz": f0,
        "time_shift_s": t0,
        "time_scale_a": a_scale
    }
    with open(os.path.join(out, "resultados.json"), "w", encoding="utf-8") as fjson:
        json.dump(results, fjson, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
