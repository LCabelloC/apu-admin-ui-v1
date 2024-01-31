import csv


def hash_password(password):
    # Selecciona un algoritmo de hash seguro, como SHA-256
    hash_algorithm = hashlib.sha256()

    # Convierte la contraseña a bytes y actualiza el objeto hash
    hash_algorithm.update(password.encode('utf-8'))

    # Obtiene el hash resultante en formato hexadecimal
    hashed_password = hash_algorithm.hexdigest()

    return hashed_password


# Ruta al archivo CSV
archivo_csv = '../data/password.csv'

# Lista para almacenar las contraseñas
contraseñas = []

# Abrir el archivo CSV en modo lectura
with open(archivo_csv, newline='', encoding='utf-8') as archivo:
    # Crear un objeto lector CSV
    lector_csv = csv.reader(archivo)

    # Ignorar la primera fila si contiene encabezados
    next(lector_csv, None)

    # Iterar sobre las filas del archivo CSV
    for fila in lector_csv:
        # Agregar la contraseña a la lista
        contraseñas.append(fila[0])

# Comprobar que la contraseña introducida coincide
    import hashlib

    password = input("Ingresa tu contraseña: ")
    hashed_password = hash_password(password)
    print("Contraseña cifrada:", hashed_password)

    if hashed_password == contraseñas[0]:
        print("Contraseña correcta")
    else:
        print("Error al introducir la contraseña")
