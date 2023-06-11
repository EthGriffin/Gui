import tkinter as tk
import math as math

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Wallpaper Ordering System")
        
        # Initialise components
        


        
class wallpaper:
    def __init__(self, rolls, paper, colour, extra, lining_paper, wallpaper_glue):
        self.rolls = rolls
        self.paper = paper
        self.colour = colour
        self.extra = extra
        self.lining_paper = lining_paper
        self.wallpaper_glue = wallpaper_glue
    
class Cart:
    def __init__(self, basket, price, total_price):
        self.basket = basket
        self.price = price
        self.total_price = total_price
    pass


if __name__ == "__main__":
    app = App()
    app.mainloop()