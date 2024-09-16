# Consolidacion_M3_LTG

# Instrucciones

Lee con atención cada uno de los requerimientos que se presentan a continuación, y desarrolla la prueba de acuerdo con lo solicitado.

## Descripción

Dada la siguiente lista de nombres:

- Harry Houdini
- Newton
- David Blaine
- Hawking
- Messi
- Teller
- Einstein
- Pele
- Juanes

Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros.

### Requerimientos

1. **Función `hacer_grandioso()`**: 
   - Modificar la lista de magos añadiendo la frase ‘El gran‘ antes del nombre de cada mago.

2. **Función `imprimir_nombres()`**: 
   - Imprimir el nombre de cada persona de la lista.

3. **Impresiones**:
   - Imprimir en pantalla la lista completa de nombres antes de ser modificados.
   - Imprimir los nombres de los magos grandiosos.
   - Imprimir los nombres de los científicos.
   - Imprimir los nombres restantes.

### Ejemplo de Implementación en Python

```python
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

# Lista de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Separar en grupos
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = [nombre for nombre in nombres if nombre not in magos + cientificos]

# Imprimir lista original
print("Lista original de nombres:")
imprimir_nombres(nombres)

# Modificar e imprimir magos grandiosos
hacer_grandioso(magos)
print("\nMagos grandiosos:")
imprimir_nombres(magos)

# Imprimir científicos
print("\nCientíficos:")
imprimir_nombres(cientificos)

# Imprimir otros
print("\nOtros:")
imprimir_nombres(otros)