import pyRserve
conn = pyRserve.connect()
try:
    # Ejecuta código R que carga el paquete BrailleR y crea un gráfico de dispersión
    conn.r('library(BrailleR)')
    conn.r('Y = rnorm(1000)')  # Cargar un conjunto de datos de ejemplo (mtcars)
    conn.r('HIST = hist(Y)')  # Abrir un dispositivo de gráficos PNG
    print(conn.r('Describe(HIST)'))
    print(conn.r('VI(HIST)'))

    conn.r('dev.off()')  # Cerrar el dispositivo de gráficos y guardar la imagen como PNG
except Exception as e:
    print(f"Error executing R code: {e}")
finally:
    # Cierra la conexión
    conn.close()