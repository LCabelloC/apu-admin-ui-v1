import csv

# Clase para el control del Login Inicial
# Gonzalo Casquete Rodriguez
# V0.0


class SocioRepository:

    # Metodo para leer los socios del fichero csv
    @classmethod
    def LoadSocios(cls, archivo_csv):
        socios = []

        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.DictReader(csvfile)

            for fila in lector_csv:
                socio = cls(
                    codigo=fila['Codigo'],
                    apellidos_nombre=fila['ApellidosNombre'],
                    nif=fila['Nif'],
                    telefono=fila['Telefono'],
                    movil=fila['Movil'],
                    banco=fila['Banco'],
                    sucursal=fila['Sucursal'],
                    dc=fila['DC'],
                    cuenta=fila['Cuenta'],
                    cuota=float(fila['Cuota']),
                    tipo_via=fila['TipoVia'],
                    calle=fila['Calle'],
                    numero=fila['Numero'],
                    planta=fila['Planta'],
                    letra=fila['Letra'],
                    poblacion=fila['Poblacion'],
                    codigo_postal=fila['CodigoPostal'],
                    provincia=fila['Provincia'],
                    email=fila['Email']
                )
                socios.append(socio)
        return socios

    # Metodo para cargar los datos en el fichero csv
    @staticmethod
    @classmethod
    def SaveSocios(socios, archivo_csv):
        with open(archivo_csv, 'w', newline='', encoding='utf-8') as csvfile:
            campos = [
                'Codigo', 'ApellidosNombre', 'Nif', 'Telefono', 'Movil', 'Banco', 'Sucursal',
                'DC', 'Cuenta', 'Cuota', 'TipoVia', 'Calle', 'Numero', 'Planta', 'Letra',
                'Poblacion', 'CodigoPostal', 'Provincia', 'Email'
            ]

            escritor_csv = csv.DictWriter(csvfile, fieldnames=campos)

            # Escribir encabezados
            escritor_csv.writeheader()

            # Escribir datos de los socios
            for socio in socios:
                escritor_csv.writerow({
                    'Codigo': socio.codigo,
                    'ApellidosNombre': socio.apellidos_nombre,
                    'Nif': socio.nif,
                    'Telefono': socio.telefono,
                    'Movil': socio.movil,
                    'Banco': socio.banco,
                    'Sucursal': socio.sucursal,
                    'DC': socio.dc,
                    'Cuenta': socio.cuenta,
                    'Cuota': socio.cuota,
                    'TipoVia': socio.tipo_via,
                    'Calle': socio.calle,
                    'Numero': socio.numero,
                    'Planta': socio.planta,
                    'Letra': socio.letra,
                    'Poblacion': socio.poblacion,
                    'CodigoPostal': socio.codigo_postal,
                    'Provincia': socio.provincia,
                    'Email': socio.email
                })

    #Metodo para eliminar al socio con codigo indicado
    @classmethod
    def DeleteSocio(cls, codigo, CsvFile):
        socios = cls.cargar_desde_csv(CsvFile)

        # Filtrar los socios para excluir el socio con el código indicado
        socios_filtrados = [
            socio for socio in socios if socio.codigo != codigo]

        # Volcar los socios filtrados de nuevo al archivo CSV
        cls.volcar_a_csv(socios_filtrados, CsvFile)
