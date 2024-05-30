import sqlite3

class Modelo:
    def __init__(self, nombre_db):
        self.nombre_db = nombre_db
        self.conexion = sqlite3.connect(self.nombre_db)
        self.crear_tabla_paciente()

    def crear_tabla_paciente(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Paciente (
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                edad INTEGER NOT NULL,
                identificacion TEXT PRIMARY KEY
            )
        ''')
        self.conexion.commit()
        cursor.close()
