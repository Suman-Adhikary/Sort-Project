from tkinter import *
from PIL import Image, ImageTk, ImageSequence
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

date2 = parser.parse(day_list[-29]['date'])
date3 = parser.parse(day_list[-21]['date'])
date4 = parser.parse(day_list[-13]['date'])
date5 = parser.parse(day_list[-5]['date'])
day2 = []
day3 = []
day4 = []
day5 = []
for i in range(0, len(day_list)):
    if (parser.parse(day_list[i]['date']).date() == date2.date()):
        day2.append(day_list[i])
    if (parser.parse(day_list[i]['date']).date() == date3.date()):
        day3.append(day_list[i])
    if (parser.parse(day_list[i]['date']).date() == date4.date()):
        day4.append(day_list[i])
    if (parser.parse(day_list[i]['date']).date() == date5.date()):
        day5.append(day_list[i])
   

first_time = '09:00:00'
first_time = (datetime.datetime.strptime(first_time, '%H:%M:%S')).time()
second_time = '15:00:00'
second_time = (datetime.datetime.strptime(second_time, '%H:%M:%S')).time()
third_time = '21:00:00'
third_time = (datetime.datetime.strptime(third_time, '%H:%M:%S')).time()

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
        canvas.create_text(600, 110, text='Today', fill='white', font=('jetbrains mono', 15, 'normal'))
        canvas.create_text(450, 160, text=f"Feel like:{day_list[0]['Feels_like']}°C  |  Pressure:{day_list[0]['Pressure']} hPa  |  Humidity:{day_list[0]['Humidity']}%", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
        canvas.create_text(460, 190, text=f"Wind speed:{day_list[0]['Wind_speed']}km/s  |  Visibility:{day_list[0]['Visibility']}km", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
    if ((day_list[0]['Weather_description'] == 'scattered clouds') or (day_list[0]['Weather_description'] == 'few clouds')):
        sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('cloudy.gif'))]
        image = canvas.create_image(450, 300, image = sequence[0])
        animate(1) 
        canvas.create_text(330, 100, text='☁️', fill='white', font=('times', 50, 'bold'))
        canvas.create_text(480, 40, text=f"{Town}, {State}", fill='white', font=('times', 36, 'normal'))
        canvas.create_text(480, 110, text=f"{day_list[0]['Temp']}°C", font=('times', 50, 'bold'), fill='white')
        canvas.create_text(600, 110, text='Today', fill='white', font=('jetbrains mono', 15, 'normal'))
        canvas.create_text(450, 160, text=f"Feel like:{day_list[0]['Feels_like']}°C  |  Pressure:{day_list[0]['Pressure']} hPa  |  Humidity:{day_list[0]['Humidity']}%", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
        canvas.create_text(460, 190, text=f"Wind speed:{day_list[0]['Wind_speed']}km/s  |  Visibility:{day_list[0]['Visibility']}km", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
    if ((day_list[0]['Weather_description'] == 'broken clouds') or (day_list[0]['Weather_description'] == 'overcast clouds') or (day_list[0]['Weather_description'] == 'light rain')):
        sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('rain.gif'))]
        image = canvas.create_image(450, 300, image = sequence[0])
        animate(1)  
        canvas.create_text(330, 100, text='⛈️', fill='white', font=('times', 50, 'bold'))
        canvas.create_text(480, 40, text=f"{Town}, {State}", fill='white', font=('times', 36, 'normal'))
        canvas.create_text(480, 110, text=f"{day_list[0]['Temp']}°C", font=('times', 50, 'bold'), fill='white')
        canvas.create_text(600, 110, text='Today', fill='white', font=('jetbrains mono', 15, 'normal'))
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
        canvas.create_text(600, 110, text='Today', fill='white', font=('jetbrains mono', 15, 'normal'))
        canvas.create_text(450, 160, text=f"Feel like:{day_list[1]['Feels_like']}°C  |  Pressure:{day_list[1]['Pressure']} hPa  |  Humidity:{day_list[1]['Humidity']}%", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
        canvas.create_text(460, 190, text=f"Wind speed:{day_list[1]['Wind_speed']}km/s  |  Visibility:{day_list[1]['Visibility']}km", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
    if ((day_list[1]['Weather_description'] == 'scattered clouds') or (day_list[1]['Weather_description'] == 'few clouds')):
        sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('cloudy.gif'))]
        image = canvas.create_image(450, 300, image = sequence[0])
        animate(1) 
        canvas.create_text(330, 100, text='☁️', fill='white', font=('times', 50, 'bold'))
        canvas.create_text(480, 40, text=f"{Town}, {State}", fill='white', font=('times', 36, 'normal'))
        canvas.create_text(480, 110, text=f"{day_list[1]['Temp']}°C", font=('times', 50, 'bold'), fill='white')
        canvas.create_text(600, 110, text='Today', fill='white', font=('jetbrains mono', 15, 'normal'))
        canvas.create_text(450, 160, text=f"Feel like:{day_list[1]['Feels_like']}°C  |  Pressure:{day_list[1]['Pressure']} hPa  |  Humidity:{day_list[1]['Humidity']}%", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
        canvas.create_text(460, 190, text=f"Wind speed:{day_list[1]['Wind_speed']}km/s  |  Visibility:{day_list[1]['Visibility']}km", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
    if ((day_list[1]['Weather_description'] == 'broken clouds') or (day_list[1]['Weather_description'] == 'overcast clouds') or (day_list[1]['Weather_description'] == 'light rain')):
        sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('rain.gif'))]
        image = canvas.create_image(450, 300, image = sequence[0])
        animate(1)  
        canvas.create_text(330, 100, text='⛈️', fill='white', font=('times', 50, 'bold'))  
        canvas.create_text(480, 40, text=f"{Town}, {State}", fill='white', font=('times', 36, 'normal')) 
        canvas.create_text(480, 110, text=f"{day_list[1]['Temp']}°C", font=('times', 50, 'bold'), fill='white')
        canvas.create_text(600, 110, text='Today', fill='white', font=('jetbrains mono', 15, 'normal'))
        canvas.create_text(450, 160, text=f"Feel like:{day_list[1]['Feels_like']}°C  |  Pressure:{day_list[1]['Pressure']} hPa  |  Humidity:{day_list[1]['Humidity']}%", fill = 'white', font = ('jetbrains mono', 15, 'normal'))
        canvas.create_text(460, 190, text=f"Wind speed:{day_list[1]['Wind_speed']}km/s  |  Visibility:{day_list[1]['Visibility']}km", fill = 'white', font = ('jetbrains mono', 15, 'normal'))        

for i in range(0, len(day2)):
    if (parser.parse(day2[i]['date']).time() == first_time):
        if(day2[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(140, 360, text=f"{parser.parse(day2[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(140, 400, text='🔆', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(140, 435, text=f"9AM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day2[i]['Weather_description'] == 'scattered clouds') or (day2[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(140, 360, text=f"{parser.parse(day3[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(140, 400, text='☁️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(140, 435, text=f"9AM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(140, 360, text=f"{parser.parse(day2[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(140, 400, text='⛈️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(140, 435, text=f"9AM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day2[i]['date']).time() == second_time):
        if(day2[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(140, 455, text=f"3PM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day2[i]['Weather_description'] == 'scattered clouds') or (day2[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(140, 455, text=f"3PM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(140, 455, text=f"3PM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day2[i]['date']).time() == third_time):
        if(day2[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(140, 475, text=f"9PM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day2[i]['Weather_description'] == 'scattered clouds') or (day2[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(140, 475, text=f"9PM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(140, 475, text=f"9PM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))

for i in range(0, len(day3)):
    if (parser.parse(day3[i]['date']).time() == first_time):
        if(day3[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(340, 360, text=f"{parser.parse(day3[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(340, 400, text='🔆', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(340, 435, text=f"9AM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day3[i]['Weather_description'] == 'scattered clouds') or (day3[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(340, 360, text=f"{parser.parse(day3[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(340, 400, text='☁️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(340, 435, text=f"9AM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(340, 360, text=f"{parser.parse(day3[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(340, 400, text='⛈️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(340, 435, text=f"9AM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day3[i]['date']).time() == second_time):
        if(day3[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(340, 455, text=f"3PM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day3[i]['Weather_description'] == 'scattered clouds') or (day3[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(340, 455, text=f"3PM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(340, 455, text=f"3PM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day3[i]['date']).time() == third_time):
        if(day3[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(340, 475, text=f"9PM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day3[i]['Weather_description'] == 'scattered clouds') or (day3[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(340, 475, text=f"9PM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(340, 475, text=f"9PM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))

for i in range(0, len(day4)):
    if (parser.parse(day4[i]['date']).time() == first_time):
        if(day4[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(540, 360, text=f"{parser.parse(day4[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(540, 400, text='🔆', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(540, 435, text=f"9AM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day4[i]['Weather_description'] == 'scattered clouds') or (day4[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(540, 360, text=f"{parser.parse(day4[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(540, 400, text='☁️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(540, 435, text=f"9AM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(540, 360, text=f"{parser.parse(day4[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(540, 400, text='⛈️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(540, 435, text=f"9AM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day4[i]['date']).time() == second_time):
        if(day4[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(540, 455, text=f"3PM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day4[i]['Weather_description'] == 'scattered clouds') or (day4[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(540, 455, text=f"3PM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(540, 455, text=f"3PM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day4[i]['date']).time() == third_time):
        if(day4[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(540, 475, text=f"9PM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day4[i]['Weather_description'] == 'scattered clouds') or (day4[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(540, 475, text=f"9PM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(540, 475, text=f"9PM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))

for i in range(0, len(day5)):
    if (parser.parse(day5[i]['date']).time() == first_time):
        if(day5[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(760, 360, text=f"{parser.parse(day5[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(760, 400, text='🔆', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(760, 435, text=f"9AM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day5[i]['Weather_description'] == 'scattered clouds') or (day5[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(760, 360, text=f"{parser.parse(day5[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(760, 400, text='☁️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(760, 435, text=f"9AM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(760, 360, text=f"{parser.parse(day5[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(760, 400, text='⛈️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(760, 435, text=f"9AM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day5[i]['date']).time() == second_time):
        if(day5[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(760, 455, text=f"3PM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day5[i]['Weather_description'] == 'scattered clouds') or (day5[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(760, 455, text=f"3PM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(760, 455, text=f"3PM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day5[i]['date']).time() == third_time):
        if(day5[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(760, 475, text=f"9PM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        elif ((day5[i]['Weather_description'] == 'scattered clouds') or (day5[i]['Weather_description'] == 'few clouds')):
            canvas.create_text(760, 475, text=f"9PM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(760, 475, text=f"9PM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
                
canvas.pack()

window.mainloop()  