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

    def agregar_paciente(self, nombre, apellido, edad, identificacion):
        cursor = self.conexion.cursor()
        try:
            cursor.execute('''
                INSERT INTO Paciente (nombre, apellido, edad, identificacion)
                VALUES (?, ?, ?, ?)
            ''', (nombre, apellido, edad, identificacion))
            self.conexion.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            cursor.close()

    def buscar_pacientes(self, nombre):
        cursor = self.conexion.cursor()
        cursor.execute('''
            SELECT * FROM Paciente
            WHERE LOWER(nombre) LIKE LOWER(?)
        ''', (nombre + '%',))
        pacientes = cursor.fetchall()
        cursor.close()
        return pacientes
