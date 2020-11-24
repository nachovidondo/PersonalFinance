import sqlite3
import os


APP_PATH=os.getcwd()
DB_PATH = APP_PATH + "gastosdatabase.db"

class Consult():
    def __init__(self):
        self.con = sqlite3.connect(DB_PATH)
        self.cursor = self.con.cursor()
        print("test",DB_PATH)
        
    def insertData(self,savedTime,textAlquiler,textAuto,textSupermercado,textServicios,textTarjetaCredito,textTransporte,textObraSocial,textRecreativos,textIngresoMama,textIngresoPapa):
         print ('debug insert', self.con, self.cursor)
         self.cursor.execute("""INSERT INTO 'Gastos Fijos' VALUES(?, ?, ?, ?, ?)""", (savedTime,textAlquiler,textServicios,textTarjetaCredito,textObraSocial))
         self.cursor.execute("""INSERT INTO 'Gastos Variables' VALUES(?, ?, ?, ?, ?)""", (savedTime,textSupermercado,textTransporte,textAuto,textRecreativos))
         self.cursor.execute("""INSERT INTO 'Ingresos' VALUES(?, ?, ?)""", (savedTime,textIngresoMama,textIngresoPapa))
         self.con.commit()
         self.con.close()
 
   
    


            
            