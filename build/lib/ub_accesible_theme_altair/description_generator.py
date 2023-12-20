import pyRserve

conn = pyRserve.connect()
try:
    # Ejecuta código R que carga el paquete BrailleR y crea un gráfico de dispersión
    conn.r('library(BrailleR)')


    conn.r('scatter = FittedLinePlot(NULL, x=rnorm(1e2), y=rnorm(1e2))')  # Cargar un conjunto de datos de ejemplo (mtcars)
    conn.r('Describe(scatter)')  # Abrir un dispositivo de gráficos PNG
    print(conn.r('hist = hist(rnorm(1e3))'))
    print(conn.r('Describe(hist)'))

    conn.r('dev.off()')  # Cerrar el dispositivo de gráficos y guardar la imagen como PNG
except Exception as e:
    print(f"Error executing R code: {e}")
finally:
    # Cierra la conexión
    conn.close()