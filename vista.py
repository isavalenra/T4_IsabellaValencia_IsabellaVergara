from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

class LoginWindow(QtWidgets.QDialog):
    def __init__(self, controlador):
        super(LoginWindow, self).__init__()
        uic.loadUi('login.ui', self)
        self.controlador = controlador
        self.pushButton_ingresar.clicked.connect(self.login)

    def login(self):
        usuario = self.lineEdit_usuario.text()
        contrasena = self.lineEdit_contrasena.text()
        if self.controlador.verificar_credenciales(usuario, contrasena):
            self.accept()
            self.controlador.mostrar_main_window()

class MainWindow(QtWidgets.QWidget):
    def __init__(self, controlador):
        super(MainWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.controlador = controlador
        self.pushButton_agregar.clicked.connect(self.agregar_paciente)
        self.pushButton_buscar.clicked.connect(self.buscar_pacientes)
        self.pushButton_cerrarSesion.clicked.connect(self.logout)
        self.pushButton_eliminar.clicked.connect(self.eliminar_paciente)

    def agregar_paciente(self):
        nombre = self.lineEdit_nombre.text()
        apellido = self.lineEdit_apellido.text()
        edad = self.lineEdit_edad.text()
        identificacion = self.lineEdit_identificacion.text()

        if self.controlador.agregar_paciente(nombre, apellido, edad, identificacion):
            self.lineEdit_nombre.clear()
            self.lineEdit_apellido.clear()
            self.lineEdit_edad.clear()
            self.lineEdit_identificacion.clear()
            QMessageBox.information(self, "Guardar", "Paciente agregado correctamente")
        else:
            QMessageBox.warning(self, "Error", "La identificación ya existe")

    def buscar_pacientes(self):
        nombre = self.lineEdit_nombre.text().strip().lower()
        if nombre == "":
            QMessageBox.warning(self, "Buscar", "Ingrese un nombre")
        else:
            pacientes = self.controlador.buscar_pacientes(nombre)
            self.tableWidget_resultadospus.clearContents()
            self.tableWidget_resultadospus.setRowCount(len(pacientes))

            for row_index, paciente in enumerate(pacientes):
                nombre, apellido, edad, identificacion = paciente
                self.tableWidget_resultadospus.setItem(row_index, 0, QTableWidgetItem(nombre))
                self.tableWidget_resultadospus.setItem(row_index, 1, QTableWidgetItem(apellido))
                self.tableWidget_resultadospus.setItem(row_index, 2, QTableWidgetItem(str(edad)))
                self.tableWidget_resultadospus.setItem(row_index, 3, QTableWidgetItem(identificacion))

    def eliminar_paciente(self):
        identificacion = self.lineEdit_identificacion.text().strip()
        if identificacion == "":
            QMessageBox.warning(self, "Eliminar", "Ingrese una identificación")
        else:
            self.controlador.eliminar_paciente(identificacion)
            self.lineEdit_identificacion.clear()
            QMessageBox.information(self, "Eliminar", "Paciente eliminado correctamente")

    def logout(self):
        self.close()
        self.controlador.mostrar_login_window()
