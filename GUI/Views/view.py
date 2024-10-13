from tkinter import *
import os
from PIL import Image, ImageTk

class View:
    def __init__(self, window, width, height):
        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()
        
        # Guardar una referencia a la imagen como un atributo de la clase
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, '..', 'images', 'river.jpg')
        image = Image.open(image_path)
        resized_image = image.resize((width, height))
        self.photo = ImageTk.PhotoImage(resized_image)  

        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
    
    def get_canvas(self):
        return self.canvas
