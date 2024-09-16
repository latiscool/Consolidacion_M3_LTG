nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes",
]


# Separa los Magos, Cientificos y otros en grupos
def nombresPorGrupo(nombres):
    grupoMago = []
    grupoCientifico = []
    Otros = []
    for m in nombres:
        if m == "Harry Houdini" or m == "David Blaine" or m == "Teller":
            grupoMago.append(m)
        elif m == "Newton" or m == "Hawking" or m == "Einstein":
            grupoCientifico.append(m)
        else:
            Otros.append(m)
    return grupoMago, grupoCientifico, Otros


# A la lista de magos le agrego el mensaje de 'El gran X'
def hacer_grandioso(magos):
    mensajeMagos = []
    for m in magos:
        mensaje = "El gran " + m
        mensajeMagos.append(mensaje)
    return mensajeMagos


def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)


# Asignamos el resultado de la funcion nombresPorGrupo que es una tupla con tres elementos
# asi que la primera lista se le asigna a grupoMago asi con las sgtes.

grupoMago, grupoCientifico, Otros = nombresPorGrupo(nombres)

# Modificamos el grupo de magos para que contengan el mensaje de la funcion hacer_grandioso
grupoMago = hacer_grandioso(grupoMago)


# Imprimir la lista completa antes de ser modificada
print("Lista de nombres:")
imprimir_nombres(nombres)
print()

# Imprimir los nombres de los magos grandiosos
print("Magos Grandiosos: ")
imprimir_nombres(grupoMago)
print()


# Imprimir los nombres de los científicos
print("Científicos:")
imprimir_nombres(grupoCientifico)
print()

# Imprimir los nombres restantes
print("Otros:")
imprimir_nombres(Otros)
print()
