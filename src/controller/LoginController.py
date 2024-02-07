# Lecturas de CSV
import csv
# Codificacion de la contraseña
import hashlib

# Clase para el control del Login Inicial
# Gonzalo Casquete Rodriguez
# V0.0


class LoginController:
    # Constructor que asigna la ruta pasada por parametro como fichero de lectura, obtiene la password y la almacena codificada
    # La ruta deberia ser ../data/password.csv
    # Param CsvFile
    @classmethod
    def __init__(self, CsvFile):
        with open(CsvFile, newline='', encoding='utf-8') as file:
            # Crear un objeto lector CSV
            lector_csv = csv.reader(file)

            # Ignorar la primera fila si contiene encabezados
            next(lector_csv, None)

            # Obtener la primera fila (suponiendo que solo hay una contraseña)
            first_row = next(lector_csv, None)

            # Extraer la contraseña de la primera fila
            password = first_row[0] if first_row else None

            self._EncryptedPassword = password
            print(password)

    # Metodo que verifica la password introducida y la almacenada en el CSV
    # Param password
    def authenticate_user(self, password):
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(password.encode('utf-8'))
        hashed_password = hash_algorithm.hexdigest()

        print(hashed_password)

        if hashed_password == self._EncryptedPassword:
            return True
        else:
            return False


# Testing
# controller = LoginController("../data/password.csv")
# contraseña_input = input("Ingrese su contraseña: ")
# controller.authenticate_user(contraseña_input)
