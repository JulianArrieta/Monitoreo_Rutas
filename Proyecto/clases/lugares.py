import sqlite3 as sql

class Lugar: 

    def __init__(self) -> None:
        self.lugar_parada = ""       

    def set_lugar_parada(self, l:str): 
        self.lugar_parada = l
    
    