import math
# Ej 1.1
def imprimir_Hola_Mundo ():
    print ("Hola mundo")
# Ej 1.2
def imprimir_Un_Verso ():
    print ("jaja \njeje \njiji")
# Ej 1.3
def raiz_De_Dos () -> float:
    return round ((math.sqrt (2)),(4))
def raiz_De (numero:int) -> float:
    return round ((math.sqrt (numero)),(4))
# Ej 1.4
def factorial_De_Dos () -> int:
    return math.factorial (2)
def factorial_De (numero:int) -> int:
    return math.factorial (numero)
# Ej 1.5
def perimetro_Radio_Uno () -> float:
    return math.pi*2
def perimetro_De (numero:int) -> float:
    return math.pi*2*(numero)
# Ej 2.1
def imprimir_Saludo (nombre:str):
    print ("Hola " + (nombre))
# Ej 2.2 ya está arriba
# Ej 2.3
def fah_A_Cel (fah:float) -> float:
    return (((fah-32)*5)/9)
# Ej 2.4
def imprimir_Dos (estribillo:str):
    print ((estribillo)*2)
# Ej 2.5
def es_Multiplo_De (m:int,n:int) -> bool:
    if (n%m) == 0:
        return True
    else:
        return False
# Ej 2.6
def es_Par (numero:int) -> bool:
    if es_Multiplo_De (2,numero) == True:
        return True
    else:
        return False
# Ej 2.7
def cant_Pizza (comensales:int, min:int) -> int:
    return math.ceil ((comensales)*(min)/8)
# Ej 3.1
def alguno_Es_Cero (n:int, m:int) -> bool:
    return n== 0 or m== 0
# Ej 3.2
def ambos_Cero (n:int, m:int) -> bool:
    return n==0 and m==0
# Ej 3.3
def es_Bisiesto (año:int) -> bool:
    return es_Multiplo_De(400,año) or (es_Multiplo_De(4,año)) and not es_Multiplo_De (100,año)
# Ej 4
def peso_piso (altura:int) -> int:
    if altura <= 300:
        return (altura *3)
    else:
        return 900 + ((altura-300)*2)
def es_Peso_Util (peso:int) -> bool:
    return (min(peso,400))== 400 and (max(peso,1000))==1000
def sirve_Pino (altura:int) -> bool:
    return es_Peso_Util (peso_piso(altura))
# Ej 5.1
def devolver_El_Doble_Si_Es_Par (x:int) -> int:
    if (x%2) == 0:
        return 2*x
    else:
        return x
# Ej 5.2
def devolver_Valor_Si_Es_Par_Sino_El_Que_Sigue (x:int) -> int:
    if (x%2) == 0:
        return x
    else: 
        return x+1
def opcion_Dos (x:int) -> int:
    if (x%2) == 0:
        return x
    if (x%2) !=0:
        return x+1
# Ej 5.3
def multiplo3_O_Multiplo9 (x:int) -> int:
  res: int = x
  if es_Multiplo_De (9,x):
    res = x*3
  else:
    if es_Multiplo_De (3,x):
      res = x*2
  return res

# Ej 5.4
def lindo_Nombre (nombre:str) -> str:
    if (len(nombre)) >= 5:
        print ("Tu nombre tiene muchas letras!")
    else:
        print ("tu nombre tiene menos de 5 caracteres")
# Ej 5.5
def el_Rango (x:int) -> str:
    if x < 5:
        print ("Tu número es menor a 5")
    else:
        if (min (10,x)) == 10 and (max(20,x)) == 20:
            print ("Entre 10 y 20")
        else:
            if (min (5,x)) == 5 and (max (9,x)) == 9 or x == 5:
                print ("Indefinido para ese número")
            else:
                print ("Mayor a 20")
# Ej 5.6
def labura_O_No (sexo:str, edad:int) -> str:
    if sexo == "F":
        if (min(18,edad))==18 and (max(60,edad))==60:
            print ("Andá a laburar")
        else:
            print ("Vacaciones")
    else: 
        if (min(18,edad))==18 and (max(65,edad))==65:
            print ("Andá a laburar")
        else:
            print ("Vacaciones")
# Ej 6.1 usar while
# Escribir una función que imprima los números del 1 al 10.
def numeros_Uno_Diez ():
    i: int = 1
    while i <= 10:
        print (i)
        i += 1 
# Ej 6.2 
# Escribir una función que imprima los números pares entre el 10 y el 40.
def solo_Pares ():
    i: int = 10
    while i <= 20:
        print (i)
        i += 2
# Ej 6.3
# Escribir una función que imprima la palabra eco 10 veces.
def eco_Diez ():
    i: int = 0
    while i < 10:
        print ("eco")
        i += 1
# Ej 6.4
# Escribir una función de cuenta regresiva para lanzar un cohete.
# Dicha función irá imprimiendo desde el número que me pasan por parámetro (que será positivo) hasta el 1, y por último Despegue.
def cuenta_Regresiva (x:int):
    while x > 0:
        print (x) 
        x -= 1
    while x == 0:
        print ("Despegue")
        x -= 1
# Ej 6.5
# Dicha función recibe dos parámetros, el año de partida y algún año de llegada,
# siendo este último parámetro siempre más chico que el primero. 
# El viaje se realizará de a saltos de un año y la función debe mostrar el texto:
# Viajó un año al pasado, estamos en el año: <año> cada vez que se realice un salto de año.     
def viajes_Tiempo (partida: int, llegada:int):
    while llegada != partida:
        partida -= 1
        print ("Viajó un año al pasado, estamos en el año:", partida)
# Ej 6.6
#Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano al 384 a.C.,
# vamos a viajar de a 20 años en cada salto.
def viajes_De20 (partida: int):
    while partida > (-364):  #para no pasarse de 384 a.C.
        partida -= 20
        print ("Viajó 20 años al pasado, estamos en el año:",partida)
    while (-384) < partida and partida < (-364):
        partida -= 1    #vuelvo a escribir la función de viajes_Tiempo ya que por la primer condición de dicha función el programa no podría cortar
        print ("Viajó un año al pasado, estamos en el año:", partida)
# Ej 7
# Implementar todos los ejercicios del 6 pero con for num in range (i,f,p)
def numeros_Uno_Diezi ():
    num: int = 1
    for num in range (1,11,1):
        print (num)
def solo_Paresi ():
    num : int = 1
    for num in range (2,21,2):
        print (num)
def eco_Diezi ():
    num: int = 0
    for num in range (1,11,1):
        print ("eco")
def cuenta_Regresivai (x:int):
    num: int = 0
    for num in range (x,num,-1): 
        print (num)
def viajes_Tiempoi (partida:int,llegada:int):
    num: int = 0
    for num in range (partida-1,llegada-1,-1):
        print ("Viajó un año al pasado, estamos en el año:",(num))
def viajes_De20i (partida:int):
    num: int = 0
    for num in range (partida-1,(-385),-20):
        print ("Viajo 20 años al pasado, estamos en el año:",(num))
'''
Ejercicio 8. Realizar la ejecución simbólica de los siguientes códigos:
1. x=5 ; y=7; x = x + y                           -----
2. x=5 ; y=7 ; z=x+y; y = z * 2                   ----- 
3. x=5 ; y=7 ; x="hora"; y = x * 2                -----
4. x=False ; res=not(x)                           -----
5. x=False ; x=not(x)                             -----
6. x=True ; y=False ; res=x and y; x = res and x  -----
???
''' 
