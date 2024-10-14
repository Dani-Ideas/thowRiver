import time
import os
from PIL import Image, ImageTk
from Models.ball import Ball
from Views.view import View
from Models.comunicator import comunicator

class Controller:
    def __init__(self, window):
        width = 500
        height = 500
        self.view = View(window, width, height)
        self.canvas = self.view.get_canvas()
        self.view.btn2.pack_forget()
        self.balls = {}

        current_dir = os.path.dirname(__file__)


        # Lista con los nombres de las imágenes
        items = ["Granjero", "Gallina", "Lobo", "Maíz"]

        # Crear instancias de Ball y añadirlas al diccionario
        for item in items:
            image_path = os.path.join(current_dir, '..', 'images', f'{item}.png')
            self.balls[item] = Ball(self.canvas, 50, 300, 1, 1, image_path)

        self.getLog = comunicator()
        self.logToPrint = self.getLog.start()
        self.index = 0
        self.top_index = len(self.logToPrint)
        self.view.btn.config(command=lambda: self.button_pressed(1))
        self.view.btn2.config(command=lambda: self.button_pressed(2))

        # Establecer las coordenadas objetivo para cada bola
        self.balls["Granjero"].set_target(50, 300)
        self.balls["Maíz"].set_target(50, 400)
        self.balls["Lobo"].set_target(50, 200)
        self.balls["Gallina"].set_target(50, 100)

    def button_pressed(self, btn_signal):

        if btn_signal == 1 and self.index < self.top_index - 1:
            self.index += 1
            self.checkCoordinate(self.logToPrint[self.index])

            if not self.view.btn2.winfo_ismapped():
                self.view.btn2.pack(side='left')
        elif btn_signal == 1 and self.index < self.top_index:
            self.view.btn.pack_forget()
            self.view.loadImage('PntExtra.jpeg')
        elif btn_signal == 2 and self.index > 0:
            self.index -= 1
            self.checkCoordinate(self.logToPrint[self.index])

            if not self.view.btn.winfo_ismapped():
                self.view.btn.pack(side='right')

            if self.index == 0:
                self.view.btn2.pack_forget()

    def start_animation(self):
        while True:
            # Mover las pelotas (acceder al diccionario)
            for ball in self.balls.values():
                ball.move()

            # Actualizar la ventana
            self.view.canvas.update()
            time.sleep(0.01)
    
    def checkCoordinate(self, coordinates):
        left_side = coordinates[0]  # Primer array (lado izquierdo)
        right_side = coordinates[1]  # Segundo array (lado derecho)

        # Recorre todas las bolas y ajusta sus coordenadas dependiendo de su posición en el log
        for name, ball in self.balls.items():
            if name in left_side:
                ball.set_target(450, ball.y)  # En el lado izquierdo
            elif name in right_side:
                ball.set_target(50, ball.y)  # En el lado derecho
