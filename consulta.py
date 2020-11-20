import sqlite3
import os


APP_PATH=os.getcwd()
DB_PATH = APP_PATH + "/gastosdatabase.db"

class Consult():
    def __init__(self):
        self.con = sqlite3.connect(DB_PATH)
        self.cursor = self.con.cursor()
        print("test",DB_PATH)
        
    def insertData(self,savedTime,textAlquiler,textAuto,textSupermercado,textServicios,textTarjetaCredito,textTransporte,textObraSocial,textRecreativos,textIngresoMama,textIngresoPapa):
         print ('debug insert', self.con, self.cursor)
         self.cursor.execute("""INSERT INTO Gastos VALUES(?, ?, ?, ?, ?, ? ,? ,? ,?)""", (textAlquiler,textAuto,textSupermercado,textServicios,textTarjetaCredito,textTransporte,textObraSocial,textRecreativos,savedTime))
         self.cursor.execute("""INSERT INTO Ingresos VALUES(?, ?, ?)""", (textIngresoMama,textIngresoPapa,savedTime))
         self.con.commit()
         self.con.close()
 
   
    


            
            