import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class App(ttk.Window):
    def __init__(self):
        #main setup
        super().__init__()
        self.title("gestion d'une pepiniere")
        self.geometry('1200x670+20+10')
        self.minsize(1200,670)
        self.nootebook=MyTabs(self,bootstyle='success')
class MyTabs(ttk.Notebook):
    def __init__(self,parent,**kyw):
        super().__init__(parent,**kyw)
        self.pepiniere=ttk.Frame(self)
        self.controle=ttk.Frame(self)
        self.suivie=ttk.Frame(self)
        self.calendrier=ttk.Frame(self)
        self.add(self.pepiniere,text='                                                 pepiniere                                                 ')
        self.add(self.controle,text='                                                controle                                                ')
        self.add(self.suivie,text='                                                suivie                                                ')
        self.add(self.calendrier,text='                                                calendrier                                                ')
        self.pack(fill=BOTH,expand=True )
        
App().mainloop()
        