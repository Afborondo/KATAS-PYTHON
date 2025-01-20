# %% [markdown]
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

# %%
def frecuencia_letras(cadena):
    lista_cadena=list(cadena)
    frecuencia={}
    for letra in lista_cadena:
        if letra==' ':
            continue
        else:
            frecuencia.update({letra:lista_cadena.count(letra)})
    print(f"frecuencia de letras de {cadena}, en formato letra: frecuencia es: {frecuencia}")
frecuencia_letras('mermelada')
frecuencia_letras('mama')

# %% [markdown]
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
# 

# %%
lista =[2,3]
doble=list(map(lambda x: x*2, lista))
print(f"el doble de {lista} es {doble}")

# %% [markdown]
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

# %%
lista_palabras=["hola", "que", "tal", "estás"]
palabra_objetivo="estás"
busca = lambda lista, objetivo: [x for x in lista if x==objetivo]
print(f"En la lista de palabras {lista_palabras} la palabra objetivo {palabra_objetivo } se ha encontrado : {busca(lista_palabras, palabra_objetivo)}")


# %% [markdown]
# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

# %%
lista_1=[1,2,3,5]
lista_2=[1,5,6,7]
diferencia=list(map(lambda x: x[0]-x[1], zip(lista_1, lista_2)))
print(f"la lista diferencia de la lista {lista_1} y {lista_2} es {diferencia}")
                

# %% [markdown]
# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

# %%
def media_estado(notas, nota_aprobado=5):
    total=0
    for i in notas: total+=i
    media=total/len(notas)
    if media>=nota_aprobado:
        estado="aprobado"
    else: 
        estado="suspenso"
    return (round(media,2), estado)
notas=[4,4,6,7,8,0]
print(f"de la lista de notas {notas} la calificación media es: {media_estado(notas)}")


# %% [markdown]
# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

# %%
def factorial(numero):
    if numero==0:
        return 1
    else:
        return numero*factorial(numero-1)

print(factorial(4))


# %% [markdown]
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

# %%
lista_tuplas=[(1,2), (3,4), (5,6)]
lista_strings= list(map(lambda x: str(x), lista_tuplas))
print(f"lista de tupla {lista_tuplas}")
print(f"lista de string {lista_strings}")

# %% [markdown]
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

# %%
try:
    numero1=int(input("escribe el primer número"))
    numero2=int(input("escribe el segundo número"))
    try:
        print(f"la división es exitosa y el resultado es : {round(numero1/numero2,2)}")
    except ZeroDivisionError:
        print("No se puede dividor por cero")
except ValueError:
    print("Valores no númericos")


# %% [markdown]
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

# %%
lista_mascotas=["perro","gato","hamster","Tigre", "Tortuga"]
lista_mascota_prohibidas=["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
resultado=list(filter(lambda x: not(bool(lista_mascota_prohibidas.count(x))), lista_mascotas))
print(f"El listado de mascotas permitidas es {resultado}")


# %% [markdown]
# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# %%
def promedio(lista_numeros):
    total=0
    try:
        for elemento in lista_numeros: 
            total+=elemento
        return(round(total/len(lista_numeros),2))
    except TypeError:
        print("Esto no es una lista de números")
        return 0
    except ValueError:
        print("Esto no es una lista de números")
        return 0
    except ZeroDivisionError:
        print("La lista está vacía")
        return 0

lista=[1,2,3,5]
media=promedio(lista)
if media:
    print(f"el promedio de {lista} es {media}")

# %% [markdown]
# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

# %%
try:
    edad=int(input("Introduce tu edad (valor númerico mayor que 0 y menor que 120):"))
except ValueError:
    print("edad errónea, valor no numérico")
else:
    if edad<=0 or edad>120:
        print(f"la edad {edad} está fuera del rango (0,120]")
    else:
        print(f"la edad {edad} es un valor correcto entre (0,120]")


# %% [markdown]
# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

# %%
frase='Esto es un frase corta'
longitud_palabras=list(map(lambda x: len(x), frase.strip().split(' ')))
print(f"la longitud de la palabras de la frase '{frase}'es {longitud_palabras}")

# %% [markdown]
# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

# %%
conjunto_caracteres={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
may_min= list(map(lambda x: (x.upper(), x.lower()), conjunto_caracteres))
print (may_min)


# %% [markdown]
# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

# %%
lista_palabras=["Hola", "que", "tal", "como", "estas"]
letra_especifica="h"
filtro_palabras=list(filter(lambda x: x.strip()[0].lower()==letra_especifica, lista_palabras))
print(f"De la lista de palabras: {lista_palabras} filtrando las que empienzan por {letra_especifica} resultan las palabras {filtro_palabras}")

# %% [markdown]
# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

# %%
lista_numeros=[1,2,3,4,5]
suma_3=list(map(lambda x: x+3, lista_numeros))
print(f"si sumanos 3 a los numeros de la lista {lista_numeros} la lista es {suma_3}")


# %% [markdown]
# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

# %%
cadena_de_texto="esto es una cadena de texto"
longitud_palabra=4
lista_palabras=list(filter(lambda x: len(x)>longitud_palabra, cadena_de_texto.strip().split(" ")))
print(f"De la cadena de texto '{cadena_de_texto}´ las palabras que exceden la longitud {longitud_palabra} son {lista_palabras}")


# %% [markdown]
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

# %%
from functools import reduce
lista_de_digitos=[1,2,2,4,5]
numero=int(reduce(lambda x,y:int(str(x)+str(y)), lista_de_digitos))
print(f"El número que corresponde a:{lista_de_digitos} es: ({numero})")


# %% [markdown]
# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

# %%
informacion_estudiantes= [{"nombre":"Ana", "edad":17, "calificación":70}, {"nombre":"Juan", "edad":18, "calificación":90}, {"nombre":"Irene", "edad":16, "calificación":95}]
estudiantes_calificados=list(filter(lambda x: x["calificación"]>=90, informacion_estudiantes))
print(f"los estudiantes con calificación mayor a 90 son: {estudiantes_calificados}")


# %% [markdown]
# 19. Crea una función lambda que filtre los números impares de una lista dada.

# %%
lista_numeros=[1,2,3,4,5,6,7,8,9]
numeros_impares= lambda x: [n for n in x if n%2!=0]
print(f"De la lista números {lista_numeros} los números impares son: {numeros_impares(lista_numeros)}")


# %% [markdown]
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

# %%
lista=["string1", 1, "string2", 2, "string3",3]
lista_int= list(filter(lambda x: type(x)==int, lista))
print(f"De la lista {lista} los de tipo entero son: {lista_int}")


# %% [markdown]
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

# %%
numero=6
cubo = lambda x: x**3
print(f"El cubo de: {numero} es {cubo(numero)}")

# %% [markdown]
# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

# %%
from functools import reduce
lista=[1,2,3,4,5,6]
producto_total=int(reduce(lambda x,y: x*y, lista))
print(f"De la lista {lista} el producto de sus números es: {producto_total}")


# %% [markdown]
# 23. Concatena una lista de palabras.Usa la función reduce() .

# %%
lista_palabras=["Esto", "es", "una", "lista", "de", "palabras"]
concatena=str(reduce(lambda x,y: str(x)+str(y), lista_palabras))
print(f"La concatenación de las palabras de la lista {lista_palabras} es: {concatena}")


# %% [markdown]
# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .
# 

# %%
lista_numeros=[1,2,3,4,5,6,7]
diferencia=int(reduce(lambda x,y: x-y, lista_numeros))
print(f"La diferencia de los números de la lista {lista_numeros} es {diferencia}")


# %% [markdown]
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

# %%
cadena_de_texto="esto es una cadena de texto"
def cuenta(cadena):
    caracteres=0
    for n in cadena:
        caracteres+=1
    return caracteres
print(f"El número de caracteres de la cadena de texto {cadena_de_texto} es {cuenta(cadena_de_texto)}")

# %% [markdown]
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# %%
número_1=4
número_2=2
division=lambda x,y: y%x
print(f"El resto de la división de {número_1} entre {número_2} es {division(número_1, número_2)}")


# %% [markdown]
# 27. Crea una función que calcule el promedio de una lista de números.

# %%
lista_numeros=[1,2,3,4,5,6,7]
def promedio(lista):
    total=0
    for numero in lista:
        total+=numero
    return round(total/numero,2)
print(f"El promedio de la lista {lista_numeros} es: {promedio(lista_numeros)}")


# %% [markdown]
# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

# %%
lista_numeros=[1,2,3,4,5,3]
def primer_duplicado(lista):
    for n in range(1, len(lista)):
        for m in range(n):
            if lista[m]==lista[n]:
                return lista[n]
    return -1
primer_repetido=primer_duplicado(lista_numeros)
if primer_repetido==-1:
    print(f"No hay números repetidos en {lista_numeros}")
else:
    print(f"El primer número de la lista {lista_numeros} que está repetido es el {primer_repetido}")

# %% [markdown]
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

# %%
variable="12312640406777"
variable_enmascarada=""
for x in range(len(variable)-4):
    variable_enmascarada+="#"
variable_enmascarada+=variable[-1:-5:-1]
print(variable_enmascarada)


# %% [markdown]
# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

# %%
palabra_1="lola"
palabra_2="lalo"
anagrama= lambda x,y: len(set(list(x)).difference(set(list(y))))
if anagrama(palabra_1, palabra_2):
    print(f" las palabras {palabra_1} y {palabra_2} no son anagramas")
else:
    print(f"las palabras {palabra_1} y {palabra_2} son anagramas")


# %% [markdown]
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

# %%
lista_nombres=set(list(input("Introduce una lista de nombres separados por ,").replace(" ","").split(',')))
nombre_buscar=input("Nombre a buscar").strip()
try:
    print(f"En la lista de nombres {lista_nombres} ")
    lista_nombres.remove(nombre_buscar)
    print(f"SÍ se ha encontrado la palabra {nombre_buscar}")
except KeyError:
     print(f"NO se ha encontrado la palabra {nombre_buscar}")



# %% [markdown]
# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

# %%
nombre_completo="Pato Donald"
lista_empleados=[{"nombre":"Pato Donald", "puesto":"puesto1"},
      {"nombre":"Mickey Mouse", "puesto":"puesto2"},
      {"nombre":"Tío Gilito", "puesto":"puesto3"}]
encontrado=False
for empleado in lista_empleados:
    if empleado["nombre"]==nombre_completo:
        print(f"El empleado cuyo nombre es: '{empleado["nombre"]}' tiene un puesto de '{empleado["puesto"]}'")
        encontrado=True
        break
if not(encontrado):
    print(f"No se ha encontrado en {lista_empleados} el empleado cuyo nombre es: '{nombre_completo}'")

# %% [markdown]
# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

# %%
lista_1=[1,2,3,4,5]
lista_2=[4,5,6,7,8]
suma_listas= lambda x,y: [(n+m) for n,m in zip(x,y)] 
print(f"La suma de elementos correspondientes de las listas {lista_1}, {lista_2} es {suma_listas(lista_1, lista_2)}")

# %% [markdown]
# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
# mismas.

# %%
class Arbol:
    def __init__(self, longitud_tronco=1, lista_ramas=[]):
        self.longitud_tronco=longitud_tronco
        if len(lista_ramas):
            self.lista_ramas=lista_ramas.copy()
        else:
            self.lista_ramas=[]
    def crecer_tronco(self):
        self.longitud_tronco+=1
    def nueva_rama(self):
        self.lista_ramas.append(1)
    def crecer_ramas(self):
        for n in range(len(self.lista_ramas)):
            self.lista_ramas[n]+=1
    def quitar_rama(self, posicion):
        self.lista_ramas.pop(posicion)
    def info_arbol(self):
       print(f"la longitud del árbol es {self.longitud_tronco}")
       print(f"la longitud de las ramas es: {self.lista_ramas}")

# %% [markdown]
# Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.

# %%
arbol1=Arbol()
arbol1.crecer_tronco()
arbol1.nueva_rama()
arbol1.crecer_ramas()
arbol1.nueva_rama()
arbol1.nueva_rama()
arbol1.quitar_rama(2)
print(arbol1.info_arbol())

# %% [markdown]
# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

# %%
class Usuariobanco:
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre=nombre
        self.saldo=saldo
        self.tiene_cuenta_corriente=tiene_cuenta_corriente
    def retirar_dinero(self, cantidad):
        if cantidad<=self.saldo:
            self.saldo-=cantidad
            return True
        else:
            return False
    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad<=self.saldo:
            self.saldo-=cantidad
            otro.usuario.saldo+=cantidad
            return True
        else:
            return False
    def agregar_dinero(self, cantidad):
        self.saldo+=cantidad



# %% [markdown]
# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente. 
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".

# %%
Alicia=Usuariobanco("Alicia", 100, True)
Bob=Usuariobanco("Bob", 50, True)
Bob.agregar_dinero(20)
if not(Bob.transferir_dinero(Alicia, 80)):
    print(f"Bob tiene un saldo de {Bob.saldo} que es insuficiente para transferir 80")
if not(Alicia.retirar_dinero(50)):
    print(f"Alicia tiene un saldo de {Alicia.saldo} que es insuficiente para retirar 50")
print(f"{Alicia.__dict__}")
print(f"{Bob.__dict__}")


# %% [markdown]
# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

# %%
def contar(texto):
    diccionario={}
    palabras=texto.split(" ")
    for palabra in palabras:
        diccionario.update({palabra:palabras.count(palabra)})
    return diccionario

def reemplazar(texto, palabra_original, palabra_nueva):
  palabras=texto.split(" ")
  texto_reemplazado=""
  for palabra in palabras:
    if palabra==palabra_original:
        texto_reemplazado+=palabra_nueva
    else:
        texto_reemplazado+=palabra
    texto_reemplazado+=" "
  return texto_reemplazado

def eliminar(texto, palabra_eliminar):
   palabras=texto.split(" ")
   texto_eliminado=""
   for palabra in palabras:
    if palabra==palabra_eliminar:
        continue
    else:
        texto_eliminado+=palabra
    texto_eliminado+=" "
   return texto_eliminado

def procesar_texto(*args):
  if args[0]==contar:
     return contar(args[1])
  elif args[0]==reemplazar:
     return reemplazar(args[1], args[2], args[3])
  elif args[0]==eliminar:
     return eliminar(args[1], args[2])

# %%
print(procesar_texto(contar, "hola la la"))

print(procesar_texto(reemplazar, "le la la", "le", "bla"))

print(procesar_texto(eliminar, "bla la la", "bla"))




# %% [markdown]
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

# %%
franjas={"7":"Noche", "12": "Mañana", "20": "Tarde", "24":"Noche"}
try:
   hora_usuario=int(input("Introduce la hora en formato HH (de 0 a 24 horas)"))
   for umbral in list(franjas.keys()):
      if int(umbral)>hora_usuario:
         franja=franjas.get(umbral)
         print(f"La franja horaria de las {hora_usuario} es: {franja}")
         break
except TypeError:
   print("Hora en formato inválido")

# %% [markdown]
# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente

# %%
notas={"70":"insuficiente", "80":"bien", "90":"muy bien", "100": "excelente" }
calificación_numérica=89
for umbral in list(notas.keys()):
    if int(umbral)>calificación_numérica:
        calificación=notas.get(umbral)
        print(f"La calficación numérica es: {calificación_numérica} y la nota es: {calificación}")
        break
 

# %% [markdown]
# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

# %%
def área(figura, datos):
    if figura=="rectángulo":
        return datos[0]*datos[1]
    elif figura=="círculo":
        return round(3.1416*(datos**2),2)
    elif figura=="triángulo":
        return datos[0]*datos[1]*0.5

print(f"El área de un rectángulo de lados 3 y 5 es {área("rectángulo", (3, 5))}")
print(f"El área de un círculo de radio es  3  {área("círculo", 3)}")
print(f"El área de un triángulo de base 3 y altura 5 es {área("triángulo", (3, 5))}")


# %% [markdown]
# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

# %%
def inputs():
    def nuevos_datos():
        print("Introduce valores válidos")
        return inputs()
    try: 
        precio_original=float(input("Introduce el precio original"))
        descuento=input("Tienes descuento? Sí/No")
        cupón=0
        precio_final=precio_original
        if descuento=="Sí":
            descuento=True
            try:
                cupón=float(input("Introduce el descuento"))
            except ValueError:
                return nuevos_datos()
            if cupón<precio_original:
                precio_final=precio_original-cupón
            else:
                print(f"cupón incorrecto, es mayor que el precio original")
                return inputs()
        elif descuento=="No":
            descuento=False
        else:
            return nuevos_datos()
        return precio_original, descuento, cupón, precio_final
    except TypeError:
        return nuevos_datos()
    except ValueError:
        return nuevos_datos()

compra=inputs()
print(f"El producto tiene un precio original {compra[0]}")
if compra[1]:
    print(f"El producto tiene descuento")
    print(f"El cupón de descuento es {compra[2]}")
    print(f"El precio final es de {compra[3]}")
else:
    print(f"El producto no tiene descuento")

# %%



