import sqlite3
import os

APP_PATH=os.getcwd()
DB_PATH = APP_PATH + "\GastosDB\gastosdatabase.db"

class Consult():
    def __init__(self):
        self.con = sqlite3.connect(DB_PATH)
        self.cursor = self.con.cursor()
        print("test",DB_PATH)
        
    def insertData(self,savedTime,textAlquiler,textAuto,textSupermercado,textServicios,textTarjetaCredito,textTransporte,textObraSocial,textRecreativos,textIngresoMama,textIngresoPapa):
         print ('debug insert', self.con, self.cursor)
         self.cursor.execute("""INSERT INTO Alquiler VALUES(?, ?, ?)""", (None,textAlquiler,savedTime))
         self.cursor.execute("""INSERT INTO Automovil VALUES(?, ?, ?)""", (None,textAuto,savedTime))
         self.cursor.execute("""INSERT INTO Obra_Social VALUES(?, ?, ?)""", (None,textObraSocial,savedTime))
         self.cursor.execute("""INSERT INTO Recreativos VALUES(?, ?, ?)""", (None,textRecreativos,savedTime))
         self.cursor.execute("""INSERT INTO Servicios VALUES(?, ?, ?)""", (None,textServicios,savedTime))
         self.cursor.execute("""INSERT INTO Supermercado VALUES(?, ?, ?)""", (None,textSupermercado,savedTime))
         self.cursor.execute("""INSERT INTO Tarjeta_Credito VALUES(?, ?, ?)""", (None,textTarjetaCredito,savedTime))
         self.cursor.execute("""INSERT INTO Transporte VALUES(?, ?, ?)""", (None,textTransporte,savedTime))
         self.cursor.execute("""INSERT INTO Ingreso_Mama VALUES(?, ?, ?)""", (None,textIngresoMama,savedTime))
         self.cursor.execute("""INSERT INTO Ingreso_Papa VALUES(?, ?, ?)""", (None,textIngresoPapa,savedTime))
         self.con.commit()
         self.con.close()
            