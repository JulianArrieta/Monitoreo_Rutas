import sqlite3 as sql
from datetime import datetime
from tkinter import messagebox

class Horario: 
    def __init__(self) -> None:
        self.h_llegada = "" 
        self.h_salida = ""
        self.fecha = datetime.today().date()
        self.fecha_str = self.fecha.strftime("%w/%m/%Y")

    def set_h_llegada(self, hora):
        try:
            obj_hora = datetime.strptime(hora, "%H:%M")
            self.h_llegada = obj_hora.time()
        except Exception:
            print(messagebox.showerror(message="Formato de hora incorrecto")) 
    
    def set_h_salida(self, hora):
        try:
            obj_hora = datetime.strptime(hora, "%H:%M")
            self.h_salida = obj_hora.time()
        except Exception:
           print(messagebox.showerror(message="Formato de hora incorrecto")) 
    def set_fecha(self, fecha:str):
        try:  
            obj_fecha = datetime.strptime(fecha, "%w/%m/%Y")
            self.fecha = obj_fecha.date() 
        except Exception:
            print(messagebox.showerror(message="Formato de fecha incorrecto"))    
    
    
print(Horario().fecha)

f = Horario()
f.set_h_salida("12:40")
print(f.h_salida)