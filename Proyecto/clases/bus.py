import sqlite3 as sql


class Bus:
   
    nombre_chofer:str = ""
    bus_num:str = ""
    id_rt:str = ""
    def set_nombre_chofer(self, n:str): 
        self.nombre_chofer = n

    def set_bus_num(self, num:str): 
        self.bus_num = num

    def set_id_rt(self, id):
        self.id_rt = id
   
        
