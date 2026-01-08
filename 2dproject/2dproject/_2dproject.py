from logging import root
import urllib.request
import json
import tkinter as Tk
from tkinter import messagebox
from tkinter import colorchooser
import time


def main_window():
    root = Tk.Tk()
    root.title("Main Window")
    root.geometry("500x500")
    root.resizable(False, False)
    return root

root = main_window()

# Title label
label = Tk.Label(root, text="🌤️ Main Window window", font=("Helvetica", 16, "bold"))
label.pack()

#Color
bg_color = '#ffffff'
open_windows = [root]

def weather_forecast():
    weather_window = Tk.Toplevel(root)
    weather_window.title("Weather Forecast")
    weather_window.geometry("350x500")
    weather_window.grab_set()
    register_window(weather_window)

def AI_App():
    AI_window=Tk.Toplevel(root)
    AI_window.tilte("AI App")
    AI_window.geometry("350x500")
    AI_window.grab_set()
    register_window(AI_window)

def Other_App():
    Other_window=Tk.Toplevel(root)
    Other_window.title("Other App")
    Other_window.geometry("350x500")
    Other_window.grab_set()
    register_window(Other_window)

def calc_app():
    calc_window = Tk.Toplevel(root)
    calc_window.title("CALC")
    calc_window.geometry("250x450")
    calc_window.grab_set()
    register_window(calc_window)

    expression = Tk.StringVar()

    
    entry = Tk.Entry(calc_window, textvariable=expression, font=("Arial", 16),
                     bd=5, relief="sunken", justify="right")
    entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

    
    def press(value):
        expr = expression.get()
        
        if value == '(' and (expr and (expr[-1].isdigit() or expr[-1] == ')')):
            expr += '*'
        elif value.isdigit() and expr and expr[-1] == ')':
            expr += '*'
        expression.set(expr + str(value))

    def clear():
        expression.set("")

    def equal():
        try:
           
            result = str(eval(expression.get()))
            expression.set(result)
        except:
            expression.set("Error")

    
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('(', 5, 0), (')', 5, 1), ('%', 5, 2), ('**', 5, 3),
        ('C', 6, 0, 4) 
    ]

    
    for button in buttons:
        if len(button) == 3:  
            text, row, col = button
            if text == "=":
                Tk.Button(calc_window, text=text, font=("Arial", 14), command=equal)\
                    .grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
            else:
                Tk.Button(calc_window, text=text, font=("Arial", 14),
                          command=lambda t=text: press(t))\
                    .grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
        else:  
            text, row, col, span = button
            Tk.Button(calc_window, text=text, font=("Arial", 14), command=clear)\
                .grid(row=row, column=col, columnspan=span, padx=3, pady=6, sticky="nsew")

    
    for i in range(7):
        calc_window.rowconfigure(i, weight=1)
    for i in range(4):
        calc_window.columnconfigure(i, weight=1)


def game_app():
    game_window = Tk.Toplevel(root)
    game_window.title("Game App")
    game_window.geometry("500x500")
    game_window.grab_set()
    register_window(game_window)


def apps():
    apps = Tk.Toplevel(root)
    apps.title("apps")
    apps.geometry("350x500")
    apps.grab_set()
    register_window(apps)


    #Weather App
    weather_button = Tk.Button(apps, text="Weather Forecast", command=weather_forecast)
    weather_button.pack(pady=20)
    #Button
    apps_button = Tk.Button(root, text="Open Apps", command=apps)
    apps_button.pack(pady=50)

    #Game App
    game_button = Tk.Button(apps, text="Game app", command=game_app)
    game_button.pack(pady=20)

    #Calc app
    calc_button = Tk.Button(apps, text="CALC", command=calc_app)
    calc_button.pack(pady=50)

    #Other App
    other_button = Tk.Button(apps, text="Other app", command=Other_App)
    other_button.pack(pady=50)


def register_window(win):
   global bg_color
   open_windows.append(win)
   win.configure(bg=bg_color)
   for widget in win.winfo_children():
        try:
            widget.configure(bg=bg_color)
        except:
            pass

def apply_theme(color):
    global bg_color
    bg_color = color
    for win in open_windows:
        try:
            win.configure(bg=bg_color)
            for widget in win.winfo_children():
                try:
                    widget.configure(bg=bg_color)
                except:
                    pass
        except:
            pass


def choose_color():
    result = colorchooser.askcolor(title="Choose background color")
    if result and result[1]:
        apply_theme(result[1])

def settings():
    settings_win = Tk.Toplevel(root)
    settings_win.title("Settings")
    settings_win.geometry("350x500")
    settings_win.grab_set()
    register_window(settings_win)


    #UI
    Tk.Label(settings_win, text="UI Customization", font=("Arial", 16, "bold")).pack(pady=20)

    #Color
    Tk.Label(settings_win, text="Background Color:", font=("Arial", 12)).pack(pady=10)
    Tk.Button(settings_win, text="Choose Color", command=choose_color).pack(pady=5)

   


def exit_app():
    root.destroy()


# Buttons

btn_settings = Tk.Button(root, text="Settings", width=20, bg="Lightblue", fg="Black", command=settings)
btn_settings.pack(pady=5)

btn_2k = Tk.Button(root, text="apps", width=20, bg="Lightblue", fg="Black", command=apps)
btn_2k.pack(pady=5)

btn_exit = Tk.Button(root, text="Exit", width=20, bg="Lightblue", fg="Black", command=exit_app)
btn_exit.pack(pady=20)

btn_exit = Tk.Button(root, text="AI", width=20, bg="Lightblue", fg="Black", command=AI_App)
btn_exit.pack(pady=20)

# Start the GUI loop
root.mainloop()