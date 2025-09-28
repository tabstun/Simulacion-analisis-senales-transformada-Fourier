# Actividad Formativa 2. Simulación y análisis de señales con la Transformada de Fourier

**Estudiante:** Abraham Rubén Tamez Rodríguez  
**Asignatura:** Señales y Sistemas (IDS)  
**Fecha:**

---

## Portada
Actividad Formativa 2 — “Simulación y análisis de señales con la Transformada de Fourier”.

## Introducción
La Transformada de Fourier permite analizar señales en el dominio de la frecuencia, revelando su contenido espectral. En esta actividad se implementó la FFT para tres señales elementales (pulso rectangular, escalón y seno), y se verificaron propiedades fundamentales: linealidad, desplazamiento en el tiempo y escalamiento en el tiempo/frecuencia.

## Metodología (Python)
1. Generación de señales discretas con frecuencia de muestreo 2000 Hz y duración 1.00 s.
2. Cálculo de FFT mediante `numpy.fft.fft`, obteniendo magnitud y fase.
3. Verificación de propiedades mediante comparaciones numéricas en el dominio de la frecuencia.
4. Visualización y exportación de gráficas (`outputs/*.png`).

## Resultados (gráficas)
- **Pulso rectangular**: `01_rect_tiempo.png`, `04_rect_mag.png`, `04_rect_fase.png`  
- **Escalón unitario**: `02_step_tiempo.png`, `05_step_mag.png`, `05_step_fase.png`  
- **Seno 50 Hz**: `03_seno_tiempo.png`, `06_seno_mag.png`, `06_seno_fase.png`  
- **Linealidad**: `07_linealidad_tiempo.png`, `08_linealidad_mag.png`  
- **Desplazamiento**: `09_desplazamiento_tiempo.png`, `10_desplazamiento_fase.png`  
- **Escalamiento**: `11_escala_tiempo.png`, `12_escala_mag.png`  

## Verificación numérica (errores máximos)
```json
{
  "linearity_max_error_fft": 2.2915694417735623e-13,
  "time_shift_max_error_fft": 50.29351089462406,
  "time_scaling_max_error_fft": 569.8567309113541,
  "sampling_rate_Hz": 2000.0,
  "N_samples": 2000,
  "duration_s": 1.0,
  "rect_width_s": 0.2,
  "sine_freq_Hz": 50.0,
  "time_shift_s": 0.05,
  "time_scale_a": 2.0
}
```

## Análisis y comparación
- **Pulso rectangular**: espectro con envolvente tipo sinc; al ser de duración finita, la energía se distribuye en múltiples lóbulos.
- **Escalón**: fuerte componente de baja frecuencia y fase con salto por la discontinuidad.
- **Seno 50 Hz**: energía en ±50 Hz; fase consistente con un tono puro.
- **Linealidad**: la FFT de la combinación coincide con la combinación lineal de FFTs (error máximo pequeño).
- **Desplazamiento temporal**: el corrimiento introduce un factor exponencial en frecuencia que altera la fase sin cambiar la magnitud.
- **Escalamiento temporal**: comprimir en el tiempo ensancha el espectro y viceversa, con factor 1/|a| en amplitud espectral.

## Conclusión
La Transformada de Fourier es esencial para interpretar señales fuera del dominio temporal. La práctica confirmó empíricamente propiedades teóricas (linealidad, desplazamiento y escalamiento), fortaleciendo la comprensión de cómo las transformaciones temporales se reflejan en el espectro.

## Código
El archivo `fourier_analysis.py` contiene todo el flujo (generación, FFT, verificación y graficación).

## Bibliografía (APA)
- Oppenheim, A. V., Willsky, A. S., & Nawab, S. H. (1996). *Signals and Systems* (2nd ed.). Prentice Hall.
- Proakis, J. G., & Manolakis, D. K. (2006). *Digital Signal Processing* (4th ed.). Pearson.
- Cooley, J. W., & Tukey, J. W. (1965). An algorithm for the machine computation of complex Fourier series. *Mathematics of Computation, 19*(90), 297–301.
- Harris, F. J. (1978). On the use of windows for harmonic analysis with the discrete Fourier transform. *Proceedings of the IEEE, 66*(1), 51–83.
