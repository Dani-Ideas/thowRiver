from PIL import Image, ImageTk
from tkinter import NW


class Ball:
    def __init__(self, canvas, x, y, xVelocity, yVelocity, image_path):
        self.canvas = canvas
        self.y=y
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.target = None  # No tiene objetivo al inicio

        self.image_file = Image.open(image_path)
        self.image_file = self.image_file.resize((50, 50))  
        self.image = ImageTk.PhotoImage(self.image_file)

        self.image_obj = self.canvas.create_image(x, y, anchor=NW, image=self.image)

    def set_target(self, target_x, target_y):
        self.target = (target_x, target_y)

    def move(self):
        if self.target:
            # Obtener coordenadas actuales
            coordinates = self.canvas.coords(self.image_obj)
            x_current = coordinates[0]
            y_current = coordinates[1]

            # Calcular diferencias para mover hacia el objetivo
            delta_x = self.target[0] - x_current
            delta_y = self.target[1] - y_current

            # Si la imagen está cerca del objetivo, se detiene
            if abs(delta_x) < abs(self.xVelocity) and abs(delta_y) < abs(self.yVelocity):
                self.xVelocity = 0
                self.yVelocity = 0
            else:
                # Actualizar velocidad para moverse hacia el objetivo
                self.xVelocity = 1 if delta_x > 0 else -1
                self.yVelocity = 1 if delta_y > 0 else -1

        # Mover la imagen
        self.canvas.move(self.image_obj, self.xVelocity, self.yVelocity)
