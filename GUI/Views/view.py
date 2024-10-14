from tkinter import *
import os
from PIL import Image, ImageTk

class View:
    def __init__(self, window, width, height):
        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()
        self.width=width
        self.height=height
        
        self.loadImage('river.jpg')

        self.btn = Button(window, text = '>>>') 
        self.btn.pack(side = 'right')  
        self.btn2 = Button(window, text = '<<<') 
        self.btn2.pack(side = 'left')  
    
    def get_canvas(self):
        return self.canvas
    
    def loadImage(self,nameimage):
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, '..', 'images', nameimage)
        image = Image.open(image_path)
        resized_image = image.resize((self.width, self.height))
        self.photo = ImageTk.PhotoImage(resized_image)  

        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
