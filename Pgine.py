import tkinter, time, keyboard, threading
from tkinter import *
from tkinter.ttk import *





def window(title="Unnamed", size="1280x720", color="white"):
    global root
    root = tkinter.Tk()
    root.configure(bg=color)
    root.title(title)
    root.geometry(size)
    return title, size, color

def loop():
    root.mainloop()

def set_pos(name, x, y):
    try:
        name.place(x=x, y=y)
    except:
        exit()
    return name, x, y

def obj(width=1, height=1, x=0, y=0, color="white", texture="photo.png"):
    name = tkinter.Button(root, width=width*2, height=height, bd=0, state="disabled", bg=color)
    name.place(x=x, y=y)
    try:
        img = PhotoImage(file=texture)
        name.configure(image=img)
    except:
        print("")
    return name

def refresh():
    try:
        root.update()
    except:
        exit()

def all_obj():
    all_obj = root.winfo_children()
    return all_obj

def key_down(key=None):
    pressed = None
    if keyboard.is_pressed(key):
        pressed = True
    else:
        pressed = False
    return pressed

def hit(obj1, obj2):
    try:
        x_obj1 = obj1.winfo_rootx()
        y_obj1 = obj1.winfo_rooty()
        height_obj1 = obj1.winfo_height()
        width_obj1 = obj1.winfo_width()
        x_obj2 = obj2.winfo_rootx()
        y_obj2 = obj2.winfo_rooty()
        height_obj2 = obj2.winfo_height()
        width_obj2 = obj2.winfo_width()
        if y_obj1+height_obj1 >= y_obj2 and x_obj1 >= x_obj2-width_obj1 and x_obj1 < x_obj2+width_obj2 and y_obj1 <= y_obj2+height_obj1:
            touching = True
        else:
            touching = False
            return touching
    except:
        print("")

def obj_pos(obj):
    x = obj.winfo_rootx()
    y = obj.winfo_rooty()
    return x, y

def text(text="", x=0, y=0, color="black", background="black", size=10, font="Courier"):
    name = tkinter.Label(text=text, fg=color, bg=background, font=(font, size))
    name.place(x=x, y=y)
    return name

def wait(sleep=0):
    time.sleep(sleep)


def kill_obj(name):
    name.place_forget()

def do_nothing():
    print("")

def button(text="", width=1, height=1, x=0, y=0, color="white", texture="photo.png", action=do_nothing, font_size=10, font="Courier", text_color="black"):
    name = tkinter.Button(root, text=text, width=width*2, height=height, bd=0, bg=color, command=action, font=(font, font_size), fg=text_color)
    name.place(x=x, y=y)
    try:
        img = PhotoImage(file=texture)
        name.configure(image=img)
    except:
        print("")
    return name