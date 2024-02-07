# Clase que representa los datos de los socios
# Gonzalo Casquete Rodriguez
# V0.0
class Socio:

    # Constructor de la clase parametrizado
    @classmethod
    def __init__(self, codigo, apellidos_nombre, nif, telefono, movil, banco, sucursal, dc, cuenta, cuota,
                 tipo_via, calle, numero, planta, letra, poblacion, codigo_postal, provincia, email):
        self.codigo = codigo
        self.apellidos_nombre = apellidos_nombre
        self.nif = nif
        self.telefono = telefono
        self.movil = movil
        self.banco = banco
        self.sucursal = sucursal
        self.dc = dc
        self.cuenta = cuenta
        self.cuota = cuota
        self.tipo_via = tipo_via
        self.calle = calle
        self.numero = numero
        self.planta = planta
        self.letra = letra
        self.poblacion = poblacion
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.email = email
