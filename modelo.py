import sqlite3

class Modelo:
    def __init__(self, nombre_db):
        self.nombre_db = nombre_db
        self.conexion = sqlite3.connect(self.nombre_db)
        self.crear_tabla_paciente()