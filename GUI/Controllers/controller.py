import time
from Models.ball import Ball
from Views.view import View

class Controller:
    def __init__(self, window):
        self.window = window  
        width = 500
        height = 500
        self.view = View(window, width, height)
        self.canvas = self.view.get_canvas()

        # Instanciación de los objetos Ball
        self.volley_ball = Ball(self.canvas, 0, 0, 100, 1, 1, "white")
        self.tennis_ball = Ball(self.canvas, 0, 0, 50, 4, 3, "yellow")
        self.basket_ball = Ball(self.canvas, 0, 0, 125, 3, 5, "orange")
        self.bowling_ball = Ball(self.canvas, 0, 0, 75, 2, 1, "black")
        self.test_ball = Ball(self.canvas, 10, 10, 75, 0, 1, "blue")


    def start_animation(self):
        while True:
            # Verificar si la ventana sigue existiendo
            if not self.window.winfo_exists():
                break  # Salir del bucle si la ventana ha sido cerrada
            
            # Mover las pelotas
            self.volley_ball.move()
            self.tennis_ball.move()
            self.basket_ball.move()
            self.bowling_ball.move()
            self.test_ball.move()
            
            # Actualizar la ventana
            self.view.canvas.update()
            time.sleep(0.01)
