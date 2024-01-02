import ttkbootstrap as ttk
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
        #weather data here
        ttk.Label(self,background='black').place(x=10,y=80,width=200,height=160)
        ttk.Label(self,text='temperature',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=90)
        ttk.Label(self,text='humidity',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=120)
        ttk.Label(self,text='pressure',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=150)
        ttk.Label(self,text='wind speed',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=180)
        ttk.Label(self,text='descreption',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=210) 
        #search box goes here
        ttk.Label(self,background='black').place(x=550,y=40,width=300,height=40)
   



App().mainloop()
        