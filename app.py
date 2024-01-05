import ttkbootstrap as ttk
from tkinter import Tk
from ttkbootstrap.constants import *
from PIL import Image,ImageTk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz

class App(ttk.Window):
    def __init__(self):
        #main setup
        super().__init__()
        self.title("gestion d'une pepiniere")
        self.geometry('1350x670+5+10')
        self.minsize(1350,670)
        icon_photo=ttk.PhotoImage(file='images/tree.png')
        self.iconphoto(False,icon_photo)

        #widgest
        self.nootebook=MyTabs(self,bootstyle='success')


class MyTabs(ttk.Notebook):
    def __init__(self,parent,**kyw):
        super().__init__(parent,**kyw)
        #main tabs
        self.pepiniere=ttk.Frame(self)
        self.controle=ttk.Frame(self)
        self.suivie=ttk.Frame(self)
        self.calendrier=ttk.Frame(self)
        self.add(self.pepiniere,text='                                                 pepiniere                                                 ')
        self.add(self.controle,text='                                                controle                                                ')
        self.add(self.suivie,text='                                                suivie                                                ')
        self.add(self.calendrier,text='                                                calendrier                                                ')
        self.pack(fill=BOTH,expand=True )
        #pepiniere tab
        Pepiniere(self.pepiniere)


class Pepiniere(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        PepiniereWeather(self).grid(column=0,row=0,sticky='nsew',columnspan=2)
        self.pack(fill=BOTH,expand=True )

class PepiniereWeather(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent,bootstyle="info")
        ##ttk variables
        self.city_var=ttk.StringVar()
        self.timezone_var=ttk.StringVar()
        self.long_lat_var=ttk.StringVar()
        #weather data here
        ttk.Label(self,background='black').place(x=10,y=80,width=200,height=160)
        ttk.Label(self,text='temperature',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=90)
        ttk.Label(self,text='humidity',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=120)
        ttk.Label(self,text='pressure',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=150)
        ttk.Label(self,text='wind speed',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=180)
        ttk.Label(self,text='descreption',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=210) 
        #search box goes here
        ttk.Label(self,background='black').place(x=550,y=40,width=400,height=45)
        self.cloud=ttk.PhotoImage(file='images/cloud.png')
        ttk.Label(self,background='black',image=self.cloud).place(x=555,y=40)
        ttk.Entry(self,font=('popins',11,'bold'),width=30,textvariable=self.city_var,foreground='black',justify='center').place(x=630,y=47)
        self.search_icon=ttk.PhotoImage(file='images/search.png')
        ttk.Button(self,image=self.search_icon,bootstyle='Dark',cursor='hand2',command=self.getweather).place(x=895,y=43)
        # days stuff goes here 
        self.days_frame=ttk.Frame(self,bootstyle='Dark')
        self.rectangle_image=ttk.PhotoImage(file='images/rectangle.png')
        self.days_image=ttk.PhotoImage(file='images/days.png')
        ttk.Label(self,background='black',image=self.rectangle_image).place(x=233,y=93)
        ttk.Label(self,background='white',image=self.days_image).place(x=480,y=120)
        ttk.Label(self,background='white',image=self.days_image).place(x=630,y=120)
        ttk.Label(self,background='white',image=self.days_image).place(x=780,y=120)
        ttk.Label(self,background='white',image=self.days_image).place(x=930,y=120)
        ttk.Label(self,background='white',image=self.days_image).place(x=1070,y=120)
        ttk.Label(self,background='white',image=self.days_image).place(x=1230,y=120)
        self.days_frame.place(x=230,y=90,width=1130,height=220)

        # time a timezone 
        ttk.Label(self,text='3:5',background="#17a2b8",font=('Helvitica',20,'bold')).place(x=20,y=20)
        ttk.Label(self,background="#17a2b8",font=('Helvitica',11),textvariable=self.timezone_var).place(x=100,y=30)
        ttk.Label(self,background="#17a2b8",font=('Helvitica',11),textvariable=self.long_lat_var).place(x=220,y=30)
        ##methodes 
    def getweather(self):
        city =self.city_var.get()
        geolocator = Nominatim(user_agent='exercice')
        location =geolocator.geocode(city)
        timezone_=TimezoneFinder()
        result=timezone_.timezone_at(lng=location.longitude,lat=location.latitude)
        self.timezone_var.set(result)
        self.long_lat_var.set(f'{round(location.latitude,4)} °N {round(location.longitude,4)} °W')


   



App().mainloop()
        