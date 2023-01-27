
import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 274.15)
    max_temp = int(json_data['main']['temp_max'] - 272.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed'] * 3.6
    sunrise = time.strftime("%H:%M:%S", time.localtime(json_data['sys']['sunrise']))
    sunset = time.strftime("%H:%M:%S", time.localtime(json_data['sys']['sunset']))
    
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "En Yüksek Sıcaklık: " + str(max_temp) + "\n" + "En Düşük Sıcaklık: " + str(min_temp) + "\n" + "Basınç: " + str(pressure) + "\n" + "Nem: " + str(humidity) + "\n" + "Rüzgar Hızı: " + str(wind) + "\n" + "Gün doğumu: " + sunrise + "\n" + "Gün batımı: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)
    
canvas = tk.Tk()
canvas.geometry("750x600")
canvas.title("Hava durumu")
canvas.button = tk.Button(canvas, text = "Hava durumu", command = lambda: getWeather(canvas))
canvas.button.pack()
canvas.button1 = tk.Button(canvas, text = "Çıkış", command = lambda: canvas.destroy())
canvas.button1.pack()

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()