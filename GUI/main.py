from tkinter import Tk
from Controllers.controller import Controller

if __name__ == "__main__":
    window = Tk()
    controller = Controller(window)
    controller.start_animation()
    window.mainloop()