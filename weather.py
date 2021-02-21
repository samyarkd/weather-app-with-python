# import Libs

import  tkinter as tk
import requests
from PIL import Image, ImageTk

# def an function that get weather info with api
def getweather(canvas):
	city = cty_input.get()
	city = str(city)
	api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=be7760d826e9776fd14ff7385ae3abac"
	print(api)
	req = requests.get(api).json()
	try:
		main_d = req["weather"][0]["main"]
		temp = req["main"]["temp"]
		temp = temp - 273.15
		temp = int(temp)
		pres = req["main"]["pressure"]
		tws = req["wind"]["speed"]
		contry_code = req["sys"]["country"]
		finfo = "Main: " + str(main_d) + "\n" + "Temp: " + str(temp) + " °C"
		fdata = "Wind speed: " + str(tws)+ " M/S" +"\n" + "Pressure: " + str(pres)
		
	
	except:
		finfo = "404"
		fdata = "City not fond"
			
	label1.config(text = finfo)
	label2.config(text = fdata)
	response = requests.get("https://www.countryflags.io/%s/flat/64.png" % contry_code)
	file = open("%s.png" % contry_code, "wb")
	file.write(response.content)
	file.close()
	image1 = Image.open("C:/Users/SkBrut/Desktop/Python Projects/%s.png" % contry_code)
	test = ImageTk.PhotoImage(image1)
	label3.config(image = test)
	


#Create canvas
canvas =  tk.Tk()
#canvas size
canvas.geometry("600x550")
#canvas Title
canvas.title("weather")

# def fonts
f  = ("cascadia mono", 15, "bold")
t  = ("cascadia mono", 35, "bold")

# get Entry from the user
cty_input = tk.Entry(canvas, font = t)
cty_input.pack(side= 'top', fill = 'x', pady = 30)
cty_input.focus()
cty_input.bind('<Return>', getweather)

# def to box for text
label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font =  f)
label2.pack()
label3 = tk.Label(canvas)
label3.pack(side = "bottom", fill = "both", expand = True)

# stop app
canvas.mainloop()
