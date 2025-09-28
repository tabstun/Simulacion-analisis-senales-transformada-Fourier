# Actividad Formativa 2 — Simulación y análisis de señales con la Transformada de Fourier

Este repositorio contiene código en **Python** para simular señales básicas (pulso rectangular, escalón y senoidal), calcular su **Transformada de Fourier (FFT)** y verificar propiedades clave: **linealidad**, **desplazamiento en el tiempo** y **escalamiento en el tiempo/frecuencia**.

## Requisitos
- Python 3.9+
- Paquetes: `numpy`, `matplotlib`

Instalación rápida:
```bash
pip install -r requirements.txt
```

## Cómo ejecutar
```bash
python fourier_analysis.py
```
Se generarán gráficas y resultados numéricos en la carpeta `outputs/`.

## Estructura
```
Actividad_Formativa_2_Fourier/
├── fourier_analysis.py
├── requirements.txt
├── README.md
├── INFORME.md
└── outputs/
    ├── 01_rect_tiempo.png
    ├── 02_step_tiempo.png
    ├── 03_seno_tiempo.png
    ├── 04_rect_mag.png
    ├── 04_rect_fase.png
    ├── 05_step_mag.png
    ├── 05_step_fase.png
    ├── 06_seno_mag.png
    ├── 06_seno_fase.png
    ├── 07_linealidad_tiempo.png
    ├── 08_linealidad_mag.png
    ├── 09_desplazamiento_tiempo.png
    ├── 10_desplazamiento_fase.png
    ├── 11_escala_tiempo.png
    ├── 12_escala_mag.png
    └── resultados.json
```

## Verificación de propiedades
Los errores máximos de verificación numérica (debidos a muestreo e interpolación) se guardan en `outputs/resultados.json`.

## Referencias (APA)
- Oppenheim, A. V., Willsky, A. S., & Nawab, S. H. (1996). *Signals and Systems* (2nd ed.). Prentice Hall.
- Proakis, J. G., & Manolakis, D. K. (2006). *Digital Signal Processing* (4th ed.). Pearson.
- Cooley, J. W., & Tukey, J. W. (1965). An algorithm for the machine computation of complex Fourier series. *Mathematics of Computation, 19*(90), 297–301.
- Harris, F. J. (1978). On the use of windows for harmonic analysis with the discrete Fourier transform. *Proceedings of the IEEE, 66*(1), 51–83.
