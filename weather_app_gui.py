# IMPORTS
from tkinter import * 
import requests
from PIL import ImageTk, Image
from tkinter import font

# VARIABLES
HEIGHT = 500
WIDTH = 600


# FUNCTION FOR FORMAT RESPONSE
def format_response(weather_json):
    try:
        name = (weather_json['name'])
        description = (weather_json['weather'][0]['description'])
        temperature = (weather_json['main']['temp'])
    
        # to pass the string values wanted
        final_str =  'City: %s \nConditions: %s \nTemperature (ºC): %s' % (name, description, temperature)

    except:
        # error in case typing error or other occurred
        final_str = 'Oops, some error occurred \nretrieving information!'

    return final_str


# FUNCTION FOR BUTTON CLICK
def get_weather(city):
    weather_key = '2e1c8bb0e5bcb30741608b9e75339af2'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    
    """
    request from server:
    App id which is the weather key
    lat value
    """
    
    results['text'] = format_response(weather)

# WINDOW
root = Tk()
root.title('Weather GUI')
root.resizable(0,0)

# CANVAS
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# BACKGROUND IMAGE
background_img = PhotoImage(file = '/home/xnm/Documents/Portfolio/Python/Weather_app/png/weather.png')
background_label = Label(root, image=background_img)
background_label.place(relwidth=1, relheight=1)

# FRAME
frame = Frame(root, bg="#80c1ff", bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.2, anchor='n')

# BUTTON
btn = Button(frame, text="Get Weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
btn.place(relx=0.7, relheight=1, relwidth=0.3)


# ENTRY
entry = Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

# LOWER FRAME
lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.2, anchor='n')

# LABEL
results = Label(lower_frame, bg='white', font=('Courier', 15), anchor='nw', justify="left", bd=4)
results.place(relheight=1, relwidth=1)

root.mainloop()