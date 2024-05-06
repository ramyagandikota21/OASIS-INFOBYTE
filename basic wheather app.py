# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:31:12 2024

@author: uppal
"""

import tkinter as tk
from tkinter import ttk
import requests

class WeatherAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        
        # Calculate the position to center the window
        window_width = 400
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        
        # Set the size and position of the window
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.label_city = tk.Label(root, text="Enter City:")
        self.label_city.pack()

        self.entry_city = tk.Entry(root)
        self.entry_city.pack()

        self.button_get_weather = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.button_get_weather.pack()

        self.label_weather_info = tk.Label(root, text="")
        self.label_weather_info.pack()

    def get_weather(self):
        city = self.entry_city.get()

        api_key = 'bdc4371d3dc48b3a9dfbb173bba90f54'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = int(data['main']['temp'] - 273.15)  # Convert temperature from Kelvin to Celsius
            desc = data['weather'][0]['main']
            weather_info = f'Current Temperature in {city} city is: {temp}°C\nCurrent Weather conditions: {desc}'
            self.label_weather_info.config(text=weather_info)
        else:
            self.label_weather_info.config(text='Error fetching weather data')

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherAppGUI(root)
    root.mainloop()
