import arcade

# Inicializar la ventana de Arcade
ANCHO_VENTANA = 640
ALTO_VENTANA = 480
arcade.open_window(ANCHO_VENTANA, ALTO_VENTANA, "Mi Dibujo")

# Establecer el color de fondo
arcade.set_background_color(arcade.color.WHITE)

# Iniciar la renderización de la ventana
arcade.start_render()

# Dibujar un círculo rojo en el centro de la ventana
arcade.draw_circle_filled(ANCHO_VENTANA/2, ALTO_VENTANA/2, 50, arcade.color.RED)

# Dibujar una línea verde desde la esquina superior izquierda hasta la esquina inferior derecha
arcade.draw_line(0, ALTO_VENTANA, ANCHO_VENTANA, 0, arcade.color.GREEN, 5)

# Finalizar la renderización de la ventana
arcade.finish_render()

# Mantener la ventana abierta hasta que se cierre manualmente
arcade.run()