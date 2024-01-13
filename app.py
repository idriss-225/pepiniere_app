import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
import tkintermapview
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
        self.personnel=ttk.Frame(self)
        self.suivie=ttk.Frame(self)
        self.calendrier=ttk.Frame(self)
        self.add(self.pepiniere,text='                                                 pepiniere                                                 ')
        self.add(self.personnel,text='                                                personnel                                                ')
        self.add(self.suivie,text='                                                suivie                                                ')
        self.add(self.calendrier,text='                                                calendrier                                                ')
        self.pack(fill=BOTH,expand=True )
        #pepiniere tab
        Pepiniere(self.pepiniere)
        #personnel tab
        Personnel(self.personnel)


class Pepiniere(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        PepiniereWeather(self).grid(column=0,row=0,sticky='nsew',columnspan=2)
        MapPepiniere(self).grid(column=0,row=1,sticky='nsew',columnspan=2)
        self.pack(fill=BOTH,expand=True )
        

class PepiniereWeather(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent,bootstyle="info")
        ##ttk variables
        self.city_var=ttk.StringVar()
        self.timezone_var=ttk.StringVar()
        self.long_lat_var=ttk.StringVar()
        self.current_time_var=ttk.StringVar()
        #weather data here
            #backgrounds
        ttk.Label(self,background='black').place(x=4,y=80,width=235,height=160)
        ttk.Label(self,text='temperature',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=90)
        ttk.Label(self,text='humidity',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=120)
        ttk.Label(self,text='pressure',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=150)
        ttk.Label(self,text='wind speed',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=180)
        ttk.Label(self,text='descreption',font=('Helvitica',11),foreground='white',background='black').place(x=14,y=210)
            #datahere
        self.temp_widget=ttk.Label(self,font=('Helvitica',11),foreground='white',background='black')
        self.temp_widget.place(x=120,y=90)
        self.humidity_widget=ttk.Label(self,font=('Helvitica',11),foreground='white',background='black')
        self.humidity_widget.place(x=120,y=120)
        self.pressure_widget=ttk.Label(self,font=('Helvitica',11),foreground='white',background='black')
        self.pressure_widget.place(x=120,y=150)
        self.wind_widget=ttk.Label(self,font=('Helvitica',11),foreground='white',background='black')
        self.wind_widget.place(x=120,y=180)
        self.description_widget=ttk.Label(self,font=('Helvitica',11),foreground='white',background='black')
        self.description_widget.place(x=120,y=210)
        #search box goes here
        ttk.Label(self,background='black').place(x=550,y=40,width=400,height=45)
        self.cloud=ttk.PhotoImage(file='images/cloud.png')
        ttk.Label(self,background='black',image=self.cloud).place(x=555,y=40)
        ttk.Entry(self,font=('popins',11,'bold'),width=30,textvariable=self.city_var,foreground='black',justify='center').place(x=630,y=47)
        self.search_icon=ttk.PhotoImage(file='images/search.png')
        ttk.Button(self,image=self.search_icon,bootstyle='Dark',cursor='hand2',command=self.getweather).place(x=895,y=43)

        # time a timezone 
        ttk.Label(self,background="#17a2b8",font=('Helvitica',20,'bold'),textvariable=self.current_time_var).place(x=20,y=20)
        ttk.Label(self,background="#17a2b8",font=('Helvitica',11),textvariable=self.timezone_var).place(x=200,y=30)
        ttk.Label(self,background="#17a2b8",font=('Helvitica',11),textvariable=self.long_lat_var).place(x=350,y=30)
        ##methodes 
    def getweather(self):
        city =self.city_var.get()
        geolocator = Nominatim(user_agent='exercice')
        location =geolocator.geocode(city)
        timezone_=TimezoneFinder()
        result=timezone_.timezone_at(lng=location.longitude,lat=location.latitude)
        self.timezone_var.set(result)
        self.long_lat_var.set(f'{round(location.latitude,2)} °N {round(location.longitude,2)} °W')
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        cuurent_time=local_time.strftime("%I:%M %p")
        self.current_time_var.set(cuurent_time)
        ## weather API
        self.api=f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid=69442d50acf30fce3842a661f12b0ed9"
        self.data=requests.get(self.api).json()
        self.temp_k=self.data['main']['temp']
        self.temp_c=round(float(self.temp_k)-274.15,2)
        self.pressure=self.data['main']['pressure']
        self.humidity=self.data['main']['humidity']
        self.wind=self.data['wind']['speed']
        self.description=self.data['weather'][0]['description']
        ## insertind data in weather widgets
        self.temp_widget.config(text=f'{self.temp_c} °C')
        self.pressure_widget.config(text=f'{self.pressure} hpa')
        self.humidity_widget.config(text=f'{self.humidity} %')
        self.wind_widget.config(text=f'{self.wind} m/s')
        self.description_widget.config(text=self.description)


class MapPepiniere(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        ## my map goes here
        self.image_pep=ttk.PhotoImage(file='images/image_pepiniere.png')
        map_widget = tkintermapview.TkinterMapView(self, width=800, height=270, corner_radius=6)
        map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.marker= map_widget.set_position(34.1526870 ,-4.1425412,marker=True,text='pepiniere z',image=(self.image_pep),image_zoom_visibility=(0, float('inf')))
        self.marker_2 = map_widget.set_marker(34.2436967 ,-4.6311753 ,text='pepiniere x')
        self.marker_3 = map_widget.set_marker(33.8662319 ,-4.6394151,text='pepiniere y')  
        map_widget.set_zoom(10)


class Personnel(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.pack(fill=BOTH,expand=True )
        Staff(self).grid(column=0,row=0,sticky='nsew')
        

class Staff(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(2,weight=1)
        self.columnconfigure(3,weight=1)
        self.columnconfigure(4,weight=1)

        self.columnconfigure(1,weight=1)
        self.staff_coldata=['ID','NOM COMPLET','TELEPHONE','SALAIRE','FONCTION','EMAIL']
        self.staff_rowdata=[]
        self.staff_table=Tableview(master=self,
                             coldata=self.staff_coldata,
                             rowdata=self.staff_rowdata,
                             searchable=True,
                             bootstyle=PRIMARY,
                             autofit=True
                             )
        self.staff_table.grid(column=4,row=0,sticky='nsw',padx=30, pady=20)
        self.data_entry=ttk.Labelframe(self)
        self.data_entry.grid(column=3,row=0,sticky='nsew')
        ttk.Label(self.data_entry,text='update').pack()
 



App().mainloop()