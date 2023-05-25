import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root_loading = Tk()
root_loading.title("Easy Cart")
root_loading.configure(bg='#393131')
root_loading.geometry('720x800')
root_loading.resizable(False, False)
root_loading.iconbitmap('icon.ico')

logo_loading = Image.open("logo.gif")
frames_loading = []

try:
    while True:
        frames_loading.append(ImageTk.PhotoImage(logo_loading))
        logo_loading.seek(len(frames_loading)) 
except EOFError:
    pass  

label_loading = Label(root_loading, image=frames_loading[0], width = 120, height = 120)
label_loading.pack()
label_loading.config(borderwidth=0)
label_loading.place(relx=0.5, rely=0.5, anchor=CENTER)

def update_loading(ind):
    frame_loading = frames_loading[ind]
    label_loading.configure(image=frame_loading)
    root_loading.after(100, update_loading, (ind+1) % len(frames_loading))

root_loading.after(0, update_loading, 0)

style = ttk.Style()
style.theme_use('clam')
style.configure("blue.Horizontal.TProgressbar", foreground='blue', background='#8C93A8')
progress = ttk.Progressbar(root_loading, orient="horizontal", length=200,
                           mode="determinate", style="blue.Horizontal.TProgressbar")
progress.pack(pady=10)
progress.place(relx=0.5, rely=0.85, anchor=CENTER)

app_name = Label(root_loading, text="Easy Cart",
                   font=("Centaur", 15, "bold"), bg='#393131', fg='white')
app_name.pack()
app_name.place(relx=0.5, rely=0.65, anchor=CENTER)

def update_progress():
    value = progress["value"]
    if value < 100:
        progress["value"] += 2
        root_loading.after(100, update_progress)
    elif value >= 100:
        root = Toplevel()
        root.title("Easy Cart")
        root.iconbitmap('icon.ico')
        root.geometry('720x800')
        root.resizable(False, False)
        root.configure(bg='#FFC2A6')
        
        image1 = Image.open("gif3.gif")
        image2 = Image.open("gif4.gif")

        frames1 = []
        frames2 = []
        try:
            while True:
                frames1.append(ImageTk.PhotoImage(image1))
                frames2.append(ImageTk.PhotoImage(image2))
                image1.seek(len(frames1)) 
                image2.seek(len(frames2))
        except EOFError:
            pass  

        label1 = Label(root, image=frames1[0])
        label2 = Label(root, image=frames2[0])
        label1.config(borderwidth=0)
        label2.config(borderwidth=0)

        label1.place(relx=0.5, rely=0.23, anchor=CENTER)
        label2.place(relx=0.5, rely=0.67, anchor=CENTER)

        def update(ind1, ind2):
            frame1 = frames1[ind1]
            frame2 = frames2[ind2]
            label1.configure(image=frame1)
            label2.configure(image=frame2)
            root.after(75, update, (ind1+1) % len(frames1), (ind2+1) % len(frames2))

        root.after(0, update, 0, 0)
        
        def open():
            window2 = Toplevel()
            window2.title("Easy Cart")
            window2.iconbitmap('icon.ico')
            window2.geometry('720x800')
            window2.resizable(False, False)
            window2.configure(bg='#FFC2A6')
            canvas = Canvas(window2, width=600, height=300)
            canvas.pack()
            canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
            #root.destroy()
            
            enter_text = Label(window2, text="Enter your app username: ",
                               font=("Roboto", 10, "bold"))
            enter_text.pack()
            enter_text.place(relx=0.5, rely=0.45, anchor='s')
            name_entry = Entry(window2, width = 50)
            name_entry.pack()
            name_entry.place(relx=0.5, rely=0.50, anchor='s')
            
            def save_name():
                global logo_pic
                name = name_entry.get()
                window2.destroy()
                window3 = Toplevel()
                window3.title("Easy Cart")
                window3.iconbitmap('icon.ico')
                window3.geometry('720x800')
                window3.resizable(False, False)
                window3.configure(bg='#FFC2A6')
                window3.columnconfigure(1, weight=1)
                
                
                display_text = Label(window3, text="Welcome to Easy Cart " 
                                     + name + "!", font=("Segoe Script", 10,
                                                         "bold italic"), bg='#FFC2A6')
                display_text.pack()
                display_text.place(relx=0.5, rely=0.11, anchor=CENTER)
                
                canvas = Canvas(window3, width=800, height=70)
                canvas.pack()
                canvas.place(relx=0, rely=0)
                logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                logo = Label(window3, image=logo_pic)
                logo.image = logo_pic
                logo.pack()
                logo.place(relx=0.47,rely=0.015)
                
            
            
                def baking_command():
                    baking_window = Toplevel()
                    baking_window.title("Easy Cart")
                    baking_window.iconbitmap('icon.ico')
                    baking_window.geometry('720x800')
                    baking_window.resizable(False, False)
                    baking_window.configure(bg='#FFC2A6')
                    baking_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(baking_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(baking_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                baking_pic = ImageTk.PhotoImage(Image.open("baking needs.png").resize((120, 120)))
                baking = Button(window3, image=baking_pic, command=baking_command)
                baking.image = baking_pic
                baking.pack()
                baking.place(relx=0.04,rely=0.13)
                
                def beverage_command():
                    beverage_window = Toplevel()
                    beverage_window.title("Easy Cart")
                    beverage_window.iconbitmap('icon.ico')
                    beverage_window.geometry('720x800')
                    beverage_window.resizable(False, False)
                    beverage_window.configure(bg='#FFC2A6')
                    beverage_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(beverage_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(beverage_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                beverage_pic = ImageTk.PhotoImage(Image.open("beverages.png").resize((120, 120)))
                beverage = Button(window3, image=beverage_pic, command=beverage_command)
                beverage.image = beverage_pic
                beverage.pack()
                beverage.place(relx=0.29,rely=0.13)
                
                def canned_command():
                    canned_window = Toplevel()
                    canned_window.title("Easy Cart")
                    canned_window.iconbitmap('icon.ico')
                    canned_window.geometry('720x800')
                    canned_window.resizable(False, False)
                    canned_window.configure(bg='#FFC2A6')
                    canned_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(canned_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(canned_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                canned_pic = ImageTk.PhotoImage(Image.open("canned goods.png").resize((120, 120)))
                canned = Button(window3, image=canned_pic, command=canned_command)
                canned.image = canned_pic
                canned.pack()
                canned.place(relx=0.54,rely=0.13)
                
                def condiments_command():
                    condiments_window = Toplevel()
                    condiments_window.title("Easy Cart")
                    condiments_window.iconbitmap('icon.ico')
                    condiments_window.geometry('720x800')
                    condiments_window.resizable(False, False)
                    condiments_window.configure(bg='#FFC2A6')
                    condiments_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(condiments_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(condiments_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                condiments_pic = ImageTk.PhotoImage(Image.open("condiments.png").resize((120, 120)))
                condiments = Button(window3, image=condiments_pic, command=condiments_command)
                condiments.image = condiments_pic
                condiments.pack()
                condiments.place(relx=0.79,rely=0.13)
                
                def dairy_command():
                    dairy_window = Toplevel()
                    dairy_window.title("Easy Cart")
                    dairy_window.iconbitmap('icon.ico')
                    dairy_window.geometry('720x800')
                    dairy_window.resizable(False, False)
                    dairy_window.configure(bg='#FFC2A6')
                    dairy_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(dairy_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(dairy_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.04,rely=0.015)
                
                dairy_pic = ImageTk.PhotoImage(Image.open("dairy.png").resize((120, 120)))
                dairy = Button(window3, image=dairy_pic, command=dairy_command)
                dairy.image = dairy_pic
                dairy.pack()
                dairy.place(relx=0.04,rely=0.30)
                
                def detergents_command():
                    detergents_window = Toplevel()
                    detergents_window.title("Easy Cart")
                    detergents_window.iconbitmap('icon.ico')
                    detergents_window.geometry('720x800')
                    detergents_window.resizable(False, False)
                    detergents_window.configure(bg='#FFC2A6')
                    detergents_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(detergents_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(detergents_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                detergents_pic = ImageTk.PhotoImage(Image.open("detergents.png").resize((120, 120)))
                detergents = Button(window3, image=detergents_pic, command=detergents_command)
                detergents.image = detergents_pic
                detergents.pack()
                detergents.place(relx=0.29,rely=0.30)
                
                def fruits_command():
                    fruits_window = Toplevel()
                    fruits_window.title("Easy Cart")
                    fruits_window.iconbitmap('icon.ico')
                    fruits_window.geometry('720x800')
                    fruits_window.resizable(False, False)
                    fruits_window.configure(bg='#FFC2A6')
                    fruits_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(fruits_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(fruits_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                fruits_pic = ImageTk.PhotoImage(Image.open("fruits.png").resize((120, 120)))
                fruits = Button(window3, image=fruits_pic, command=fruits_command)
                fruits.image = fruits_pic
                fruits.pack()
                fruits.place(relx=0.54,rely=0.30)
                
                def health_command():
                    health_window = Toplevel()
                    health_window.title("Easy Cart")
                    health_window.iconbitmap('icon.ico')
                    health_window.geometry('720x800')
                    health_window.resizable(False, False)
                    health_window.configure(bg='#FFC2A6')
                    health_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(health_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(health_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                health_pic = ImageTk.PhotoImage(Image.open("health.png").resize((120, 120)))
                health = Button(window3, image=health_pic, command=health_command)
                health.image = health_pic
                health.pack()
                health.place(relx=0.79,rely=0.30)
                
                def laundry_command():
                    laundry_window = Toplevel()
                    laundry_window.title("Easy Cart")
                    laundry_window.iconbitmap('icon.ico')
                    laundry_window.geometry('720x800')
                    laundry_window.resizable(False, False)
                    laundry_window.configure(bg='#FFC2A6')
                    laundry_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(laundry_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(laundry_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                laundry_pic = ImageTk.PhotoImage(Image.open("laundry aids.png").resize((120, 120)))
                laundry = Button(window3, image=laundry_pic, command=laundry_command)
                laundry.image = laundry_pic
                laundry.pack()
                laundry.place(relx=0.04,rely=0.47)
                
                def meats_command():
                  meats_window = Toplevel()
                  meats_window.title("Easy Cart")
                  meats_window.iconbitmap('icon.ico')
                  meats_window.geometry('720x800')
                  meats_window.resizable(False, False)
                  meats_window.configure(bg='#FFC2A6')
                  meats_window.columnconfigure(1, weight=1)
                  
                  canvas = Canvas(meats_window, width=800, height=70)
                  canvas.pack()
                  canvas.place(relx=0, rely=0)
                  logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                  logo = Label(meats_window, image=logo_pic)
                  logo.image = logo_pic
                  logo.pack()
                  logo.place(relx=0.47,rely=0.015)
              
                meats_pic = ImageTk.PhotoImage(Image.open("meats.png").resize((120, 120)))
                meats = Button(window3, image=meats_pic, command=meats_command)
                meats.image = meats_pic
                meats.pack()
                meats.place(relx=0.29,rely=0.47)
                
                def oats_command():
                  oats_window = Toplevel()
                  oats_window.title("Easy Cart")
                  oats_window.iconbitmap('icon.ico')
                  oats_window.geometry('720x800')
                  oats_window.resizable(False, False)
                  oats_window.configure(bg='#FFC2A6')
                  oats_window.columnconfigure(1, weight=1)
                  
                  canvas = Canvas(oats_window, width=800, height=70)
                  canvas.pack()
                  canvas.place(relx=0, rely=0)
                  logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                  logo = Label(oats_window, image=logo_pic)
                  logo.image = logo_pic
                  logo.pack()
                  logo.place(relx=0.47,rely=0.015)
              
                oats_pic = ImageTk.PhotoImage(Image.open("oats.png").resize((120, 120)))
                oats = Button(window3, image=oats_pic, command=oats_command)
                oats.image = oats_pic
                oats.pack()
                oats.place(relx=0.54,rely=0.47)
                
                def oil_command():
                    oil_window = Toplevel()
                    oil_window.title("Easy Cart")
                    oil_window.iconbitmap('icon.ico')
                    oil_window.geometry('720x800')
                    oil_window.resizable(False, False)
                    oil_window.configure(bg='#FFC2A6')
                    oil_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(oil_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(oil_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                oil_pic = ImageTk.PhotoImage(Image.open("oil.png").resize((120, 120)))
                oil = Button(window3, image=oil_pic, command=oil_command)
                oil.image = oil_pic
                oil.pack()
                oil.place(relx=0.79,rely=0.47)
                
                def pasta_command():
                    pasta_window = Toplevel()
                    pasta_window.title("Easy Cart")
                    pasta_window.iconbitmap('icon.ico')
                    pasta_window.geometry('720x800')
                    pasta_window.resizable(False, False)
                    pasta_window.configure(bg='#FFC2A6')
                    pasta_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(pasta_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(pasta_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                pasta_pic = ImageTk.PhotoImage(Image.open("pasta.png").resize((120, 120)))
                pasta = Button(window3, image=pasta_pic, command=pasta_command)
                pasta.image = pasta_pic
                pasta.pack()
                pasta.place(relx=0.04,rely=0.64)
                
                def pastries_command():
                    pastries_window = Toplevel()
                    pastries_window.title("Easy Cart")
                    pastries_window.iconbitmap('icon.ico')
                    pastries_window.geometry('720x800')
                    pastries_window.resizable(False, False)
                    pastries_window.configure(bg='#FFC2A6')
                    pastries_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(pastries_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(pastries_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                pastries_pic = ImageTk.PhotoImage(Image.open("pastries.png").resize((120, 120)))
                pastries = Button(window3, image=pastries_pic, command=pastries_command)
                pastries.image = pastries_pic
                pastries.pack()
                pastries.place(relx=0.29,rely=0.64)
                
                def pet_command():
                    pet_window = Toplevel()
                    pet_window.title("Easy Cart")
                    pet_window.iconbitmap('icon.ico')
                    pet_window.geometry('720x800')
                    pet_window.resizable(False, False)
                    pet_window.configure(bg='#FFC2A6')
                    pet_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(pet_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(pet_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                pet_pic = ImageTk.PhotoImage(Image.open("pet.png").resize((120, 120)))
                pet = Button(window3, image=pet_pic, command=pet_command)
                pet.image = pet_pic
                pet.pack()
                pet.place(relx=0.54,rely=0.64)
                
                def rice_command():
                    rice_window = Toplevel()
                    rice_window.title("Easy Cart")
                    rice_window.iconbitmap('icon.ico')
                    rice_window.geometry('720x800')
                    rice_window.resizable(False, False)
                    rice_window.configure(bg='#FFC2A6')
                    rice_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(rice_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(rice_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                rice_pic = ImageTk.PhotoImage(Image.open("rice.png").resize((120, 120)))
                rice = Button(window3, image=rice_pic, command=rice_command)
                rice.image = rice_pic
                rice.pack()
                rice.place(relx=0.79,rely=0.64)
                
                def snacks_command():
                    snacks_window = Toplevel()
                    snacks_window.title("Easy Cart")
                    snacks_window.iconbitmap('icon.ico')
                    snacks_window.geometry('720x800')
                    snacks_window.resizable(False, False)
                    snacks_window.configure(bg='#FFC2A6')
                    snacks_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(snacks_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(snacks_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                snacks_pic = ImageTk.PhotoImage(Image.open("snacks.png").resize((120, 120)))
                snacks = Button(window3, image=snacks_pic, command=snacks_command)
                snacks.image = snacks_pic
                snacks.pack()
                snacks.place(relx=0.04,rely=0.81)
                
                def spreads_command():
                    spreads_window = Toplevel()
                    spreads_window.title("Easy Cart")
                    spreads_window.iconbitmap('icon.ico')
                    spreads_window.geometry('720x800')
                    spreads_window.resizable(False, False)
                    spreads_window.configure(bg='#FFC2A6')
                    spreads_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(spreads_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(spreads_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                spreads_pic = ImageTk.PhotoImage(Image.open("spreads.png").resize((120, 120)))
                spreads = Button(window3, image=spreads_pic, command=spreads_command)
                spreads.image = spreads_pic
                spreads.pack()
                spreads.place(relx=0.29,rely=0.81)
                
                def vegetables_command():
                    vegetables_window = Toplevel()
                    vegetables_window.title("Easy Cart")
                    vegetables_window.iconbitmap('icon.ico')
                    vegetables_window.geometry('720x800')
                    vegetables_window.resizable(False, False)
                    vegetables_window.configure(bg='#FFC2A6')
                    vegetables_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(vegetables_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(vegetables_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                
                vegetables_pic = ImageTk.PhotoImage(Image.open("vegetables.png").resize((120, 120)))
                vegetables = Button(window3, image=vegetables_pic, command=vegetables_command)
                vegetables.image = vegetables_pic
                vegetables.pack()
                vegetables.place(relx=0.54,rely=0.81)
                
                def add_command():
                    add_window = Toplevel()
                    add_window.title("Easy Cart")
                    add_window.iconbitmap('icon.ico')
                    add_window.geometry('720x800')
                    add_window.resizable(False, False)
                    add_window.configure(bg='#FFC2A6')
                    add_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(add_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(add_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                    
                    my_tree = ttk.Treeview(add_window)
                    storeName = "Add an Item"


                    def reverse(tuples):
                        new_tup = tuples[::-1]
                        return new_tup


                    def insert( id, name, price, quantity):
                        conn = sqlite3.connect("eclist1.db")
                        cursor = conn.cursor()

                        cursor.execute("""CREATE TABLE IF NOT EXISTS 
                        inventory(itemId TEXT, itemName TEXT, itemPrice TEXT
                                  , itemQuantity TEXT)""")

                        cursor.execute("INSERT INTO inventory VALUES ('" + str(id) +
                                       "','" + str(name) + "','" + str(price) + "','"
                                       + str(quantity) + "')")
                        conn.commit()


                    def delete(data):
                        conn = sqlite3.connect("eclist1.db")
                        cursor = conn.cursor()

                        cursor.execute("""CREATE TABLE IF NOT EXISTS 
                            inventory(itemId TEXT, itemName TEXT, itemPrice TEXT,
                                      itemQuantity TEXT)""")

                        cursor.execute("DELETE FROM inventory WHERE itemId = '" +
                                       str(data) + "'")
                        conn.commit()


                    def update(id, name, price, quantity,  idName):
                        conn = sqlite3.connect("eclist1.db")
                        cursor = conn.cursor()

                        cursor.execute("""CREATE TABLE IF NOT EXISTS 
                            inventory(itemId TEXT, itemName TEXT, itemPrice TEXT,
                                      itemQuantity TEXT)""")

                        cursor.execute("UPDATE inventory SET itemId = '" 
                                       + str(id) + "', itemName = '" 
                                       + str(name) + "', itemPrice = '" 
                                       + str(price) + "', itemQuantity = '" 
                                       + str(quantity) + "' WHERE itemId='"
                                       +str(idName)+"'")
                        conn.commit()


                    def read():
                        conn = sqlite3.connect("eclist1.db")
                        cursor = conn.cursor()

                        cursor.execute("""CREATE TABLE IF NOT EXISTS 
                            inventory(itemId TEXT, itemName TEXT, itemPrice TEXT,
                                      itemQuantity TEXT)""")

                        cursor.execute("SELECT * FROM inventory")
                        results = cursor.fetchall()
                        conn.commit()
                        return results


                    def insert_data():
                        itemId = str(entryId.get())
                        itemName = str(entryName.get())
                        itemPrice = str(entryPrice.get())
                        itemQuantity = str(entryQuantity.get())
                        if itemId == "" or itemName == " ":
                            print("Error Inserting Item Number")
                        if itemName == "" or itemName == " ":
                            print("Error Inserting Name")
                        if itemPrice == "" or itemPrice == " ":
                            print("Error Inserting Price")
                        if itemQuantity == "" or itemQuantity == " ":
                            print("Error Inserting Quantity")
                        else:
                            insert(str(itemId), str(itemName), str(itemPrice),
                                   str(itemQuantity))

                        for data in my_tree.get_children():
                            my_tree.delete(data)

                        for result in reverse(read()):
                            my_tree.insert(parent='', index='end', iid=result, text="",
                                           values=(result), tag="orow")

                        my_tree.tag_configure('orow', background='#EEEEEE')
                        my_tree.pack()
                        my_tree.place(relx=0.09,rely=0.55)


                    def delete_data():
                        selected_item = my_tree.selection()[0]
                        deleteData = str(my_tree.item(selected_item)['values'][0])
                        delete(deleteData)

                        for data in my_tree.get_children():
                            my_tree.delete(data)

                        for result in reverse(read()):
                            my_tree.insert(parent='', index='end', iid=result, text="",
                                           values=(result), tag="orow")

                        my_tree.tag_configure('orow', background='#EEEEEE')
                        my_tree.pack()
                        my_tree.place(relx=0.09,rely=0.55)

                    def update_data():
                        selected_item = my_tree.selection()[0]
                        update_name = my_tree.item(selected_item)['values'][0]
                        update(entryId.get(), entryName.get(), entryPrice.get(),
                               entryQuantity.get(), update_name)

                        for data in my_tree.get_children():
                            my_tree.delete(data)

                        for result in reverse(read()):
                            my_tree.insert(parent='', index='end', iid=result, text="",
                                           values=(result), tag="orow")

                        my_tree.tag_configure('orow', background='#EEEEEE')
                        my_tree.pack()
                        my_tree.place(relx=0.09,rely=0.55)


                    titleLabel = Label(add_window, text=storeName,
                                       font=('Roboto', 30, 'bold'), bd=2, bg='#FFC2A6')
                    titleLabel.pack()
                    titleLabel.place(relx=0.34,rely=0.1)

                    idLabel = Label(add_window, text="Item No.", font=('Roboto bold', 15),
                                    bg='#FFC2A6')
                    nameLabel = Label(add_window, text="Item Name", font=('Roboto bold', 15),
                                      bg='#FFC2A6')
                    priceLabel = Label(add_window, text="Price", font=('Roboto bold', 15),
                                       bg='#FFC2A6')
                    quantityLabel = Label(add_window, text="Quantity",
                                          font=('Roboto bold', 15), bg='#FFC2A6')
                    idLabel.pack()
                    nameLabel.pack()
                    priceLabel.pack()
                    quantityLabel.pack()
                    idLabel.place(relx=0.1,rely=0.20)
                    nameLabel.place(relx=0.1,rely=0.25)
                    priceLabel.place(relx=0.1,rely=0.30)
                    quantityLabel.place(relx=0.1,rely=0.35)

                    entryId = Entry(add_window, width=25, bd=5, font=('Roboto', 15, 'bold'))
                    entryName = Entry(add_window, width=25, bd=5, font=('Roboto', 15, 'bold'))
                    entryPrice = Entry(add_window, width=25, bd=5
                                       , font=('Roboto', 15, 'bold'))
                    entryQuantity = Entry(add_window, width=25, bd=5,
                                          font=('Roboto', 15, 'bold'))
                    entryId.pack()
                    entryName.pack()
                    entryPrice.pack()
                    entryQuantity.pack()
                    entryId.place(relx=0.31,rely=0.20)
                    entryName.place(relx=0.31,rely=0.25)
                    entryPrice.place(relx=0.31,rely=0.30)
                    entryQuantity.place(relx=0.31,rely=0.35)

                    buttonEnter = Button(
                        add_window, text="Add", padx=5, pady=5, width=5,
                        bd=3, font=('Roboto', 15), bg="#DAEAF6", command=insert_data)
                    buttonEnter.pack()
                    buttonEnter.place(relx=0.35,rely=0.44)

                    buttonUpdate = Button(
                        add_window, text="Update", padx=5, pady=5, width=5,
                        bd=3, font=('Roboto', 15), bg="#DDEDEA", command=update_data)
                    buttonUpdate.pack()
                    buttonUpdate.place(relx=0.45,rely=0.44)

                    buttonDelete = Button(
                        add_window, text="Delete", padx=5, pady=5, width=5,
                        bd=3, font=('Roboto', 15), bg="#FCE1E4", command=delete_data)
                    buttonDelete.pack()
                    buttonDelete.place(relx=0.55,rely=0.44)

                    style = ttk.Style()
                    style.configure("Treeview.Heading", font=('Roboto', 15, 'bold'))

                    my_tree['columns'] = ("ID", "Name", "Price", "Quantity")
                    my_tree.column("#0", width=0, stretch=NO)
                    my_tree.column("ID", anchor=W, width=100)
                    my_tree.column("Name", anchor=W, width=200)
                    my_tree.column("Price", anchor=W, width=150)
                    my_tree.column("Quantity", anchor=W, width=150)
                    my_tree.heading("ID", text="Item No.", anchor=W)
                    my_tree.heading("Name", text="Item Name", anchor=W)
                    my_tree.heading("Price", text="Price", anchor=W)
                    my_tree.heading("Quantity", text="Quantity", anchor=W)

                    for data in my_tree.get_children():
                        my_tree.delete(data)

                    for result in reverse(read()):
                        #error
                        my_tree.insert(parent='', index='end', iid=0, text="",
                                       values=(result), tag="orow")

                    my_tree.tag_configure('orow', background='#EEEEEE',
                                          font=('Roboto bold', 15))
                    my_tree.pack()
                    my_tree.place(relx=0.09,rely=0.55)
                
                add_pic = ImageTk.PhotoImage(Image.open("add item.png").resize((100, 100)))
                add = Button(window3, image=add_pic, command=add_command, width= 120, height= 55)
                add.image = add_pic
                add.pack()
                add.place(relx=0.79,rely=0.81)
                
                def list_command():
                    list_window = Toplevel()
                    list_window.title("Easy Cart")
                    list_window.iconbitmap('icon.ico')
                    list_window.geometry('720x800')
                    list_window.resizable(False, False)
                    list_window.configure(bg='#FFC2A6')
                    list_window.columnconfigure(1, weight=1)
                    
                    canvas = Canvas(list_window, width=800, height=70)
                    canvas.pack()
                    canvas.place(relx=0, rely=0)
                    logo_pic = ImageTk.PhotoImage(Image.open("logo.png").resize((50, 50)))
                    logo = Label(list_window, image=logo_pic)
                    logo.image = logo_pic
                    logo.pack()
                    logo.place(relx=0.47,rely=0.015)
                    
                    
                
                list_pic = ImageTk.PhotoImage(Image.open("show list.png").resize((100, 100)))
                list = Button(window3, image=list_pic, command=list_command, width= 120, height= 55)
                list.image = list_pic
                list.pack()
                list.place(relx=0.79,rely=0.89)


               
            
            save_btn = Button(window2, text="Create a list", command=save_name,
                              width=12, height=1,
                               bg="white", fg="black", font=("Roboto", 10, "bold"))
            save_btn.pack()
            save_btn.place(relx=0.5, rely=0.55, anchor='s')
            
        enter_btn = Button(root, text = "Let's get started!", command=open, width=15, height=1,
                           bg="white", fg="black", font=("Roboto", 10, "bold"))
        enter_btn.place(relx=0.5, rely=0.95, anchor='s')

update_progress()

root_loading.mainloop()
