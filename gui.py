import tkinter as tk
import math as math

root = tk.Tk()

root.title("Wallpaper Ordering System")

frame = tk.Frame(root)
frame.pack()

# Functions
order = {
    "Rolls": 0,
    "Paper": None,
    "Pattern": None,
    "Colour": None,
    "Extras": None,
    "Added": {"LP": None, "WG": None}
}

def order_selection(option_type, selection):
        # Check if button is already selected
    if order[option_type] == selection:
        # Unselect button
        order[option_type] = None
        reset_button_color(option_type)
    elif option_type == "Added" and order[option_type]["LP"] == selection:
        order[option_type]["LP"] = None
        print("yoyoyoyo")
        reset_button_color(option_type, selection)
    elif option_type == "Added" and order[option_type]["WG"] == selection:
        order[option_type]["WG"] = None
        reset_button_color(option_type, selection)
    else:
        # Update dictionary with selected button name
        if option_type == "Added":
            if selection == "Lining paper":
                order[option_type]["LP"] = selection
            elif selection == "Wallpaper glue":
                order[option_type]["WG"] = selection
        else:
            order[option_type] = selection

        # Turn off previous selected button color
        reset_button_color(option_type)

        # Turn on selected button color
        if order[option_type] == "cheap":
            paper_button1.configure(bg="gray74")
        if order[option_type] == "expensive":
            paper_button2.configure(bg="gray74")
        if order[option_type] == "Pattern 1":
            pattern_button1.configure(bg="gray74")
        if order[option_type] == "Pattern 2":
            pattern_button2.configure(bg="gray74")
        if order[option_type] == "Foil":
            extras_button1.configure(bg="gray74")
        if order[option_type] == "Glitter":
            extras_button2.configure(bg="gray74")
        if order[option_type] == "Embossing":
            extras_button3.configure(bg="gray74")
        if order[option_type] == "None":
            extras_button4.configure(bg="gray74")
        if option_type == "Added":
            if order[option_type]["LP"] == "Lining paper":
                addon_button1.configure(bg="gray74")
            if order[option_type]["WG"] == "Wallpaper glue":
                addon_button2.configure(bg="gray74")
    
    # changes wallpaper design and colour dependent on option for pattern
    if order["Pattern"] == None:
        canvas.delete('all')
    elif order["Pattern"] == "Pattern 1":
        create_wallpaper1("purple")
    elif order["Pattern"] == "Pattern 2":
        create_wallpaper2("purple")
    if order["Colour"] in dropdownValues and order["Pattern"] != None:
        colour = colourChoice.get()
        
        if order["Pattern"] == "Pattern 1":
            create_wallpaper1(colour)
        elif order["Pattern"] == "Pattern 2":
            create_wallpaper2(colour)


    print(order)

def reset_button_color(option_type, selection="Nothing"):

        # Reset color of all buttons for a given option type
    if option_type == "Paper":
        paper_button1.configure(bg="grey94")
        paper_button2.configure(bg="grey94")
    elif option_type == "Pattern":
        pattern_button1.configure(bg="grey94")
        pattern_button2.configure(bg="grey94")
    elif option_type == "Extras":
        extras_button1.configure(bg="grey94")
        extras_button2.configure(bg="grey94")
        extras_button3.configure(bg="grey94")
        extras_button4.configure(bg="grey94")
    elif option_type == "Added" and selection == "Lining paper":
        addon_button1.configure(bg="grey94")
    elif option_type == "Added" and selection == "Wallpaper glue":
        addon_button2.configure(bg="grey94")


# Create order frame
order_frame = tk.LabelFrame(frame)
order_frame.grid(row=0, column=0, padx=(10,5), pady=10)

# ---- Order frame functionality ----

# Wallpaper length

lengthInputFrame = tk.Frame(order_frame)
lengthInputFrame.grid(row=0, column=0)

label = tk.Label(lengthInputFrame, text="Wallpaper Length:", font=('Arial', 12))
label.grid(sticky="W", row=0, column=0, padx=10, pady=(20))

wallpaper_value = tk.StringVar()

rolls = 0

def my_callback(var, index, mode):
    print (f"Traced variable {wallpaper_value.get()}")
    if wallpaper_value.get() != "":
        rolls = int(float(wallpaper_value.get())//10.05)
        if float(wallpaper_value.get())%10.05 != 0:
            rolls += 1
        value_sign.config(text=rolls)

wallpaper_value.trace_add('write', my_callback)

length = tk.Entry(lengthInputFrame, textvariable=wallpaper_value)
length.grid(sticky="W", row=0, column=1, pady=(20))

def callback(input):
    if input == "":
        print(input)
        return True

    else:
        try: 
            float(input)
            print(input)
            return True
        except ValueError:
            print(input)
            return False

reg = lengthInputFrame.register(callback)

length.config(validate ="key", 
         validatecommand =(reg, '%P'))


m_sign = tk.Label(lengthInputFrame, text="m", font=('Arial', 12))
m_sign.grid(sticky="W", row=0, column=2, padx=(0,10), pady=(20))

rolls_sign = tk.Label(lengthInputFrame, text="Rolls:", font=('Arial', 12))
rolls_sign.grid(row=0, column=3, padx=(0,10), pady=(20))

value_sign = tk.Label(lengthInputFrame, text="0", font=('Arial', 12), width=4)
value_sign.grid(row=0, column=4, padx=(0,10), pady=(20))




# Paper type

paperInputFrame = tk.Frame(order_frame)
paperInputFrame.grid(row=1, column=0)

label = tk.Label(paperInputFrame, text="Paper:", font=('Arial', 12))
label.grid(sticky="W", row=0, column=0)

paper_button1 = tk.Button(paperInputFrame, font=('Arial', 12), text="Cheap", command= lambda: order_selection("Paper", "cheap"), bg="grey94")
paper_button1.grid(sticky="W", row=0, column=1, padx=10, pady=20)

paper_button2 = tk.Button(paperInputFrame, text="Expensive", font=('Arial', 12), command= lambda: order_selection("Paper", "expensive"), bg="grey94")
paper_button2.grid(sticky="W", row=0, column=2, padx=10, pady=20)


# Pattern choice

patternInputFrame = tk.Frame(order_frame)
patternInputFrame.grid(row=2, column=0)

label = tk.Label(patternInputFrame, text="Pattern:", font=('Arial', 12))
label.grid(sticky="W", row=0, column=0)

pattern_button1 = tk.Button(patternInputFrame, text="Pattern 1", font=('Arial', 12), command= lambda: order_selection("Pattern", "Pattern 1"), bg="grey94")
pattern_button1.grid(sticky="W", row=0, column=1, padx=10, pady=20)

pattern_button2 = tk.Button(patternInputFrame, text="Pattern 2", font=('Arial', 12), command= lambda: order_selection("Pattern", "Pattern 2"), bg="grey94")
pattern_button2.grid(sticky="W", row=0, column=2, padx=10, pady=20)


# Colour choice

colourInputFrame = tk.Frame(order_frame)
colourInputFrame.grid(row=3, column=0)

label = tk.Label(colourInputFrame, text="Colour:", font=('Arial', 12))
label.grid(sticky="W", row=0, column=0, padx=10, pady=20)

colourChoice = tk.StringVar(colourInputFrame)

dropdownValues = ["Purple", "DarkSlateGray4", "Deep sky blue" ,"Light sea green", "VioletRed2", "Gold"]

def callback(selection):
    order_selection("Colour", selection)
dropdown = tk.OptionMenu(colourInputFrame, colourChoice, *dropdownValues, command= callback)
dropdown.config(bg="grey94", activebackground="grey74")
dropdown.grid(sticky="W", row=0, column=1)

# Extras

extraInputFrame = tk.Frame(order_frame)
extraInputFrame.grid(row=4, column=0)

label = tk.Label(extraInputFrame, text="Extras:", font=('Arial', 12))
label.grid(sticky="W", row=0, column=0, padx=10, pady=20)

extras_button1 = tk.Button(extraInputFrame, text="Foil", font=('Arial', 12), command= lambda: order_selection("Extras", "Foil"), bg="grey94")
extras_button1.grid(sticky="W", row=0, column=1, padx=10, pady=20)

extras_button2 = tk.Button(extraInputFrame, text="Glitter", font=('Arial', 12), command= lambda: order_selection("Extras", "Glitter"), bg="grey94")
extras_button2.grid(sticky="W", row=0, column=2, padx=10, pady=20)

extras_button3 = tk.Button(extraInputFrame, text="Embossing", font=('Arial', 12), command= lambda: order_selection("Extras", "Embossing"), bg="grey94")
extras_button3.grid(sticky="W", row=0, column=3, padx=10, pady=20)

extras_button4 = tk.Button(extraInputFrame, text="None", font=('Arial', 12), command= lambda: order_selection("Extras", "None"), bg="grey94")
extras_button4.grid(sticky="W", row=0, column=4, padx=10, pady=20)

# Add ons

AddOnsInputFrame = tk.Frame(order_frame)
AddOnsInputFrame.grid(row=5, column=0)

label = tk.Label(AddOnsInputFrame, text="Add:", font=('Arial', 12))
label.grid(sticky="W", row=0, column=0, padx=10, pady=20)

addon_button1 = tk.Button(AddOnsInputFrame, text="Add Lining Paper", font=('Arial', 12), command= lambda: order_selection("Added", "Lining paper"), bg="grey94")
addon_button1.grid(sticky="W", row=0, column=1, padx=10, pady=20)


addon_button2 = tk.Button(AddOnsInputFrame, text="Add Wallpaper Glue", activebackground="dark grey", font=('Arial', 12), command= lambda: order_selection("Added", "Wallpaper glue"), bg="grey94")
addon_button2.grid(sticky="W", row=0, column=2, padx=10, pady=20)






# Create preview frame
preview_frame = tk.LabelFrame(frame, text="Preview", labelanchor="n")
preview_frame.grid(row=0, column=1, padx=(5,10), pady=10)

# ---- Preview frame functionality ----

# Canvas
canvas = tk.Canvas(preview_frame, width=300, height=300, bg="white")
canvas.grid(row=0, column=0, padx=20, pady=20)

def create_wallpaper1(colour):
    canvas.delete('all')
    for x in [-1, 0, 1, 2, 3]:
        for y in [0, 1, 2, 3, 4]:
            if (y in [1, 3, 5]):
                coords = [30+90*x, 30+60*y, 60+90*x, 0+60*y, 90+90*x, 0+60*y, 120+90*x, 30+60*y, 90+90*x, 60+60*y, 60+90*x, 60+60*y]
            else:
                coords = [0+90*x, 30+60*y, 30+90*x, 0+60*y, 60+90*x, 0+60*y, 90+90*x, 30+60*y, 60+90*x, 60+60*y, 30+90*x, 60+60*y]
            canvas.create_polygon(coords, fill=colour, outline="black", width=3)

def create_wallpaper2(colour):
    canvas.delete('all')
    for i in [4, 3, 2, 1, 0]:
        coords_TL = 120-30*i, 120-30*i, 180-30*i, 180-30*i
        coords_TR = 120+30*i, 120-30*i, 180+30*i, 180-30*i
        coords_BL = 120-30*i, 120+30*i, 180-30*i, 180+30*i
        coords_BR = 120+30*i, 120+30*i, 180+30*i, 180+30*i
        rec1 = canvas.create_rectangle(coords_TL, fill=colour, outline=colour, width=3)
        rec2 = canvas.create_rectangle(coords_TR, fill=colour, outline=colour, width=3)
        rec3 = canvas.create_rectangle(coords_BL, fill=colour, outline=colour, width=3)
        rec4 = canvas.create_rectangle(coords_BR, fill=colour, outline=colour, width=3)
        
        if i in [1, 3]:
            canvas.itemconfig(rec1, fill="white")
            canvas.itemconfig(rec2, fill="white")
            canvas.itemconfig(rec3, fill="white")
            canvas.itemconfig(rec4, fill="white")

# Pricing

complete_frame = tk.Frame(preview_frame)
complete_frame.grid(row=1, column=0, padx=20, pady=20)

price = tk.Label(complete_frame, text="Price:", font=('Arial', 12))
price.grid(row=0, column=0, padx=10, pady=10)

def add_to_basket():
    for selections in [order["Colour"], order["Pattern"], order["Paper"]]:
        if selections == None:
            print("no way Josue")
# def Pricing():
 

# Completion



Add_to_basket_button = tk.Button(complete_frame, text="Add to Basket", font=('Arial', 12), command=add_to_basket)
Add_to_basket_button.grid(row=1, column=0, padx=10, pady=10)






root.mainloop()