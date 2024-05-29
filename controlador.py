import sys
from PyQt5 import QtWidgets
from modelo import Modelo
from vista import LoginWindow, MainWindow

class Controlador:
    def __init__(self, modelo):
        self.modelo = modelo
        self.login_window = None
        self.main_window = None

    def verificar_credenciales(self, usuario, contrasena):
        return usuario == "admin123" and contrasena == "contrasena123"  # admin123 , contrasena123

    def mostrar_login_window(self):
        self.login_window = LoginWindow(self)
        self.login_window.exec_()

    def mostrar_main_window(self):
        self.main_window = MainWindow(self)
        self.main_window.show()

    def agregar_paciente(self, nombre, apellido, edad, identificacion):
        if self.modelo.agregar_paciente(nombre, apellido, edad, identificacion):
            return True
        else:
            return False

    def buscar_pacientes(self, nombre):
        return self.modelo.buscar_pacientes(nombre)

    def eliminar_paciente(self, identificacion):
        self.modelo.eliminar_paciente(identificacion)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    modelo = Modelo('base.db')
    controlador = Controlador(modelo)
    controlador.mostrar_login_window()
    sys.exit(app.exec_())
