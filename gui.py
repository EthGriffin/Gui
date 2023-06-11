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
    "Colour": None,
    "Extras": None,
    "Added": {"LP": None, "WG": None}
}

total_price = tk.StringVar()
total_price.set(0)
cart_total = tk.StringVar()
cart_total.set(0)

def order_selection(option_type, selection):
        # Check if button is already selected
    if order[option_type] == selection:
        # Unselect button
        order[option_type] = None
        reset_button_color(option_type)
    elif option_type == "Added" and order[option_type]["LP"] == selection:
        order[option_type]["LP"] = None
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
        if order[option_type] == "Cheap":
            paper_button1.configure(bg="light sky blue")
        if order[option_type] == "Expensive":
            paper_button2.configure(bg="light sky blue")
        if order[option_type] == "Foil":
            extras_button1.configure(bg="light sky blue")
        if order[option_type] == "Glitter":
            extras_button2.configure(bg="light sky blue")
        if order[option_type] == "Embossing":
            extras_button3.configure(bg="light sky blue")
        if order[option_type] == "No extras":
            extras_button4.configure(bg="light sky blue")
        if option_type == "Added":
            if order[option_type]["LP"] == "Lining paper":
                addon_button1.configure(bg="light sky blue")
            if order[option_type]["WG"] == "Wallpaper glue":
                addon_button2.configure(bg="light sky blue")
    
    # changes wallpaper design and colour dependent on option for pattern
    if order["Paper"] == None:
        canvas.delete('all')
    elif order["Paper"] == "Cheap":
        create_wallpaper1("purple")
    elif order["Paper"] == "Expensive":
        create_wallpaper2("purple")
    if order["Colour"] in dropdownValues and order["Paper"] != None:
        colour = colourChoice.get()
        
        if order["Paper"] == "Cheap":
            create_wallpaper1(colour)
        elif order["Paper"] == "Expensive":
            create_wallpaper2(colour)


    print(order)
    total_price.set(str(Pricing()))

def reset_button_color(option_type, selection="Nothing"):

        # Reset color of all buttons for a given option type
    if option_type == "Paper":
        paper_button1.configure(bg="grey94")
        paper_button2.configure(bg="grey94")
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

def my_callback(var, index, mode):
    print (f"Traced variable {wallpaper_value.get()}")
    if wallpaper_value.get() != "":
        rolls = int(float(wallpaper_value.get())//10.05)
        if float(wallpaper_value.get())%10.05 != 0:
            rolls += 1
        value_sign.config(text=rolls)
    
    order["Rolls"] = rolls
    print(order)


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

paper_button1 = tk.Button(paperInputFrame, font=('Arial', 12), text="Cheap", command= lambda: order_selection("Paper", "Cheap"), bg="grey94")
paper_button1.grid(sticky="W", row=0, column=1, padx=10, pady=20)

paper_button2 = tk.Button(paperInputFrame, text="Expensive", font=('Arial', 12), command= lambda: order_selection("Paper", "Expensive"), bg="grey94")
paper_button2.grid(sticky="W", row=0, column=2, padx=10, pady=20)


# Colour choice

colourInputFrame = tk.Frame(order_frame)
colourInputFrame.grid(row=3, column=0)

label = tk.Label(colourInputFrame, text="Colour:", font=('Arial', 12))
label.grid(sticky="W", row=0, column=0, padx=10, pady=20)

colourChoice = tk.StringVar(colourInputFrame)

dropdownValues = ["Purple", "DarkSlateGray4", "light sky blue" ,"Light sea green", "VioletRed2", "Gold"]

def callback_colour(selection):
    order_selection("Colour", selection)
dropdown = tk.OptionMenu(colourInputFrame, colourChoice, *dropdownValues, command= callback_colour)
dropdown.config(bg="grey94", activebackground="Light sky blue")
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

extras_button4 = tk.Button(extraInputFrame, text="None", font=('Arial', 12), command= lambda: order_selection("Extras", "No extras"), bg="grey94")
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
canvas.grid(row=1, column=0, padx=20, pady=20)

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

def reset_order():
    order["Rolls"] = 0
    order["Paper"] = None
    order["Colour"] = None
    order["Extras"] = None
    order["Added"]["LP"] = None
    order["Added"]["WG"] = None
    wallpaper_value.set(0)
    wallpaper_value.set("")
    colourChoice.set("")
    total_price.set(0)
    canvas.delete('all')
    for option in order:
        if option == "Added":
            print("hello added is working")
            reset_button_color(option, "Lining paper")
            reset_button_color(option, "Wallpaper glue")
        else:
            reset_button_color(option)
            
basket = []
basket_total = []
def add_to_basket():

    # add order to basket
    order_screenshot = str(order)
    basket.append(order_screenshot)
    order_price = Pricing()
    if order_price is False:
        print("Uh uh, not a chance")
    else:
        basket_total.append(order_price)
        print(basket, basket_total)
        cart_total.set(sum(basket_total))
        reset_order()
    # TODO: need to clear the wallpaper length input as well and rolls


        
        
    

def Pricing():
    
    # Check if order is complete
    if order["Rolls"] == 0 or order["Colour"] is None or order["Paper"] is None or order["Extras"] is None:
        print("no way Josue")
        return False
        
        
    rolls = order["Rolls"]
    area = rolls * 5.226 # Amount of Rolls * 5.226m2 per roll

    # wallpaper price for Cheap or Expensive
    if order["Paper"] == "Cheap":
        wallpaper_price = area * 30 # area * £30 per m2
    elif order["Paper"] == "Expensive":
        wallpaper_price = area * 60 # area * £60 per m2
    
    extras_price_dict = {"Foil": 0.12, "Glitter": 0.18, "Embossing": 0.06, "No extras": 0}
    extras_price = rolls * 10.05 * extras_price_dict[order["Extras"]]
    print(order["Extras"], rolls, extras_price_dict[order["Extras"]], extras_price)

    if order["Added"]["LP"] == "Lining paper":
        lining_paper_rolls = float(wallpaper_value.get())//20
        if float(wallpaper_value.get())%20 != 0:
            lining_paper_rolls += 1
        lining_paper_price = lining_paper_rolls * 7.63
    else: lining_paper_price = 0
    
    if order["Added"]["WG"] == "Wallpaper glue":
        if order["Added"]["LP"] == "Lining paper":
            tub_quantity = ((rolls*5.226) + lining_paper_rolls * 10.4) // 53
            if ((rolls*5.226) + lining_paper_rolls * 10.4)%53 != 0:
                tub_quantity += 1
        else:
            tub_quantity = int((rolls*5.226)//53)
            if (rolls*5.226)%53 != 0:
                tub_quantity += 1
        glue_price = tub_quantity * 13.99
    else: glue_price = 0


    
    order_price = wallpaper_price + extras_price + glue_price + lining_paper_price # TODO: round this to 2 d.p.
    print(wallpaper_price, extras_price, glue_price, lining_paper_price)
    return round(order_price, 2)



# Completion

def cart():
    window = tk.Toplevel(root)
    window.title("Cart")
    
    order_labels = []
    # order_labels = {}
    # orders_to_delete = []
      
    def delete_order(index):
        order_labels[index].destroy()
        del order_labels[index]
        del basket_total[index]
        cart_total.set(round(sum(basket_total), 2))
        del basket[index]
        window.destroy()
        cart()
        reciept()
        
        
    for i, item in enumerate(basket):
        order_label = tk.Label(window, text=f"Order {i+1}:     {item}, Price: £{basket_total[i]}")
        order_label.grid(row=i, column=0, padx=10, pady=10)
        order_labels.append(order_label)

        cancel_this_order = tk.Button(window, text="Delete", command=lambda index=i: delete_order(index))
        cancel_this_order.grid(row=i, column=1, padx=10, pady=10)


        
        
        
    
cart_frame = tk.Frame(preview_frame)
cart_frame.grid(row=0, column=0, padx=(5,10), pady=10)
cart_button = tk.Button(cart_frame, text="Cart", command=cart)
cart_button.grid(sticky="E", row=0, column=0, padx=10, pady=10)
total_price_in_cart = tk.Label(cart_frame, textvariable=cart_total) # TODO: update with total price of everything in cart
total_price_in_cart.grid(sticky="E", row=0, column=1, padx=10, pady=10)


price_frame = tk.Frame(preview_frame)
price_frame.grid(row=2, column=0, padx=(5,10), pady=10)
price_text = tk.Label(price_frame, text="Price:     £", font=('Arial', 12))
price_text.grid(row=0, column=0, padx=(10,0), pady=10)
price = tk.Label(price_frame, textvariable=total_price, font=('Arial', 12))
price.grid(row=0, column=1, pady=10)

basket_button_frame = tk.Frame(preview_frame)
basket_button_frame.grid(row=3, column=0, padx=(5,10), pady=10)
Add_to_basket_button = tk.Button(basket_button_frame, text="Add to Basket", font=('Arial', 12), command=add_to_basket)
Add_to_basket_button.grid(row=0, column=0, padx=10, pady=10)



# print order to a txt file

def reciept():
    
    order_json = []
    
    for i, order in enumerate(basket):
        order_data = {
            'order_number' : i+1,
            'order' : order,
            'price' : basket_total[i]
        }
        order_json.append(order_data)
    
    order_json.append({'total_price' : sum(basket_total)})
    f = open("Receipt.txt", "w")
    f.write(str(order_json))
tk.Button(basket_button_frame, text="Complete", command=reciept).grid(row=1, column=0, padx=10, pady=10)
root.mainloop()