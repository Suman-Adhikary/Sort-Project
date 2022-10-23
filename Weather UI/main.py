from tkinter import *
from PIL import Image, ImageTk, ImageSequence
from matplotlib.pyplot import text
import requests
from dateutil import parser
import datetime
import math

API = "b744285416bdf9133f32148bb25a0edf"

Town = input('Enter your town/villege name : ').title()
State = input('Enter your state code : ').upper()
Country = input('Enter your country code : ').upper()

Parameter = {
    'q' : [Town, State, Country],
    'appid' : API,
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=Parameter)
response.raise_for_status()

data = response.json()['list']
location = response.json()['city']

day_list = []
for i in range(0, len(data)):
    day_list.append('data' + str(i))   

################################################ Weather Data ############################################

for i in range(0, len(data)):
    day_list[i] = {
        "Temp" : math.ceil(data[i]['main']['temp'] - 273.15),
        "Feels_like" : math.ceil(data[i]['main']['feels_like'] - 273.15),
        "Pressure" : data[i]['main']['pressure'],
        "Humidity" : data[i]['main']['humidity'],
        "Weather_description" : data[i]['weather'][0]['description'],
        "Wind_speed" : math.ceil(data[i]['wind']['speed'] / 1000),
        "Visibility" : math.ceil(data[i]['visibility'] / 1000),
        "date" : data[i]['dt_txt']
    }

current_time = datetime.datetime.now()
      

time0 = parser.parse(day_list[0]['date'])
time1 = parser.parse(day_list[1]['date'])
time2 = parser.parse(day_list[2]['date'])

################################################# weather UI ###############################################

window = Tk()
canvas = Canvas(window, width=900, height=600)
def animate(counter):
    canvas.itemconfig(image, image = sequence[counter])
    window.after(33, lambda: animate((counter+1) % len(sequence)))

if time0 <= current_time < time1:
    if (day_list[0]['Weather_description'] == 'clear sky'):
        sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('sky.gif'))]
        image = canvas.create_image(450, 300, image = sequence[0])
        animate(1)
        canvas.create_text(330, 100, text='🔆', fill='white', font=('times', 50, 'bold'))
        canvas.create_text(480, 40, text=f"{Town}, {State}", fill='white', font=('times', 36, 'normal'))
        canvas.create_text(480, 110, text=f"{day_list[0]['Temp']}°C", font=('times', 50, 'bold'), fill='white')
        canvas.create_text(450, 160, text=f"Feel like:{day_list[0]['Feels_like']}°C  |  Pressure:{day_list[0]['Pressure']} hPa  |  Humidity:{day_list[0]['Humidity']}%", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
        canvas.create_text(460, 190, text=f"Wind speed:{day_list[0]['Wind_speed']}km/s  |  Visibility:{day_list[0]['Visibility']}km", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
    if ((day_list[0]['Weather_description'] == 'scattered clouds') or (day_list[0]['Weather_description'] == 'few clouds')):
        sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('cloudy.gif'))]
        image = canvas.create_image(450, 300, image = sequence[0])
        animate(1) 
        canvas.create_text(330, 100, text='☁️', fill='white', font=('times', 50, 'bold'))
        canvas.create_text(480, 40, text=f"{Town}, {State}", fill='white', font=('times', 36, 'normal'))
        canvas.create_text(480, 110, text=f"{day_list[0]['Temp']}°C", font=('times', 50, 'bold'), fill='white')
        canvas.create_text(450, 160, text=f"Feel like:{day_list[0]['Feels_like']}°C  |  Pressure:{day_list[0]['Pressure']} hPa  |  Humidity:{day_list[0]['Humidity']}%", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
        canvas.create_text(460, 190, text=f"Wind speed:{day_list[0]['Wind_speed']}km/s  |  Visibility:{day_list[0]['Visibility']}km", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
    if ((day_list[0]['Weather_description'] == 'broken clouds') or (day_list[0]['Weather_description'] == 'overcast clouds')):
        sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('rain.gif'))]
        image = canvas.create_image(450, 300, image = sequence[0])
        animate(1)  
        canvas.create_text(330, 100, text='⛈️', fill='white', font=('times', 50, 'bold'))
        canvas.create_text(480, 40, text=f"{Town}, {State}", fill='white', font=('times', 36, 'normal'))
        canvas.create_text(480, 110, text=f"{day_list[0]['Temp']}°C", font=('times', 50, 'bold'), fill='white')
        canvas.create_text(450, 160, text=f"Feel like:{day_list[0]['Feels_like']}°C  |  Pressure:{day_list[0]['Pressure']} hPa  |  Humidity:{day_list[0]['Humidity']}%", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
        canvas.create_text(460, 190, text=f"Wind speed:{day_list[0]['Wind_speed']}km/s  |  Visibility:{day_list[0]['Visibility']}km", fill = 'white', font = ('jetbrains mono', 15, 'normal'))

elif time1 <= current_time < time2:
    if (day_list[1]['Weather_description'] == 'clear sky'):
        sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('sky.gif'))]
        image = canvas.create_image(450, 300, image = sequence[0])
        animate(1)
        canvas.create_text(330, 100, text='🔆', fill='white', font=('times', 50, 'bold'))
        canvas.create_text(480, 40, text=f"{Town}, {State}", fill='white', font=('times', 36, 'normal'))
        canvas.create_text(480, 110, text=f"{day_list[1]['Temp']}°C", font=('times', 50, 'bold'), fill='white')
        canvas.create_text(450, 160, text=f"Feel like:{day_list[1]['Feels_like']}°C  |  Pressure:{day_list[1]['Pressure']} hPa  |  Humidity:{day_list[1]['Humidity']}%", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
        canvas.create_text(460, 190, text=f"Wind speed:{day_list[1]['Wind_speed']}km/s  |  Visibility:{day_list[1]['Visibility']}km", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
    if ((day_list[1]['Weather_description'] == 'scattered clouds') or (day_list[1]['Weather_description'] == 'few clouds')):
        sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('cloudy.gif'))]
        image = canvas.create_image(450, 300, image = sequence[0])
        animate(1) 
        canvas.create_text(330, 100, text='☁️', fill='white', font=('times', 50, 'bold'))
        canvas.create_text(480, 40, text=f"{Town}, {State}", fill='white', font=('times', 36, 'normal'))
        canvas.create_text(480, 110, text=f"{day_list[1]['Temp']}°C", font=('times', 50, 'bold'), fill='white')
        canvas.create_text(450, 160, text=f"Feel like:{day_list[1]['Feels_like']}°C  |  Pressure:{day_list[1]['Pressure']} hPa  |  Humidity:{day_list[1]['Humidity']}%", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
        canvas.create_text(460, 190, text=f"Wind speed:{day_list[1]['Wind_speed']}km/s  |  Visibility:{day_list[1]['Visibility']}km", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
    if ((day_list[1]['Weather_description'] == 'broken clouds') or (day_list[1]['Weather_description'] == 'overcast clouds')):
        sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('rain.gif'))]
        image = canvas.create_image(450, 300, image = sequence[0])
        animate(1)  
        canvas.create_text(330, 100, text='⛈️', fill='white', font=('times', 50, 'bold'))  
        canvas.create_text(480, 40, text=f"{Town}, {State}", fill='white', font=('times', 36, 'normal')) 
        canvas.create_text(480, 110, text=f"{day_list[1]['Temp']}°C", font=('times', 50, 'bold'), fill='white')
        canvas.create_text(450, 160, text=f"Feel like:{day_list[1]['Feels_like']}°C  |  Pressure:{day_list[1]['Pressure']} hPa  |  Humidity:{day_list[1]['Humidity']}%", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
        canvas.create_text(460, 190, text=f"Wind speed:{day_list[1]['Wind_speed']}km/s  |  Visibility:{day_list[1]['Visibility']}km", fill = 'white', font = ('jetbrains mono', 15, 'normal'))        

canvas.create_text(140, 400, text='⛈️', fill='white', font=('times', 30, 'normal'))
canvas.create_text(300, 400, text='🔆', fill='white', font=('times', 30, 'normal'))
canvas.create_text(450, 400, text='⛅', fill='white', font=('times', 30, 'normal'))
canvas.create_text(600, 400, text='☁️', fill='white', font=('times', 30, 'normal'))
canvas.create_text(750, 400, text='🌦️', fill='white', font=('times', 30, 'normal'))

canvas.pack()

window.mainloop()  