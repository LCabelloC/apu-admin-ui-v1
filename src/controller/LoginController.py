import csv
import hashlib
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from secrets import compare_digest  # Para comparación segura de cadenas


class LoginController(QMainWindow):
    # Constructor, inicia ventana inicial
    def __init__(self):
        super(LoginController, self).__init__()
        loadUi('../view/LoginPage.ui', self)

        self.pushButton.clicked.connect(self.authenticate_user)
        self.MainView = None

    def authenticate_user(self):
        # Obtenemos campo de la ventana y la codificamos
        password = self.lineEdit.text()

        # La codificamos
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Obtenemos campo del csv
        try:
            with open('../data/password.csv', 'r') as file:
                # Crear un objeto lector csv
                lector_csv = csv.reader(file)

                # Ignorar la primera fila si contiene encabezados
                next(lector_csv, None)

                # Obtener la primera fila (suponiendo que solo hay una contraseña)
                first_row = next(lector_csv, None)

                # Extraer la contraseña de la primera fila
                passwordCsv = first_row[0] if first_row else None

            # Verificamos y redirigimos
            if compare_digest(passwordCsv, hashed_password):
                self.MainView = MainController()
                self.MainView.show()
                self.close()
            else:
                print("Contraseña incorrecta.")
        except FileNotFoundError:
            print("Archivo CSV no encontrado.")
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")


class MainController(QMainWindow):
    def __init__(self):
        super(MainController, self).__init__()
        loadUi('../view/MainPage.ui', self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_controller = LoginController()
    login_controller.show()
    sys.exit(app.exec_())
