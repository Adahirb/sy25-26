import tkinter as tk
from tkinter import messagebox, simpledialog
from pyowm import OWM

def weather_map():
    messagebox.showinfo("Weather Map", "Going to Weather Map...")

def current_weather():
    messagebox.showinfo("Current Weather", "Fechting current weather...")

def settings():
    messagebox.showinfo("Settings", "Opening settings...")

def exit_app():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("2k26")
root.geometry("400x400")
root.resizable(False, False)

# Title label
label = tk.Label(root, text="🌤️ 2K26", font=("Helvetica", 16, "bold"))
label.pack(pady=20)

# Buttons
btn_current = tk.Button(root, text="weather map", width=20, bg="Lightblue", fg="Black", command=weather_map)
btn_current.pack(pady=5)

btn_forecast = tk.Button(root, text="current weather", width=20, bg="Lightblue", fg="Black", command=current_weather)
btn_forecast.pack(pady=5)

btn_settings = tk.Button(root, text="Settings", width=20, bg="Lightblue", fg="Black", command=settings)
btn_settings.pack(pady=5)

btn_exit = tk.Button(root, text="Exit", width=20, bg="Lightblue", fg="Black", command=exit_app)
btn_exit.pack(pady=20)

# Start the GUI loop
root.mainloop()