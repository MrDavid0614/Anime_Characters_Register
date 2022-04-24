from os import system
from pick import pick
from time import sleep
from opciones import *

def gestionar_personajes():
    system("cls")
    opciones = ['1- Añadir personaje', '2- Editar personaje', '3- Borrar personaje']
    opcion, _ = pick(opciones, '----- Gestionar Personajes -----', indicator="->")
    opcion = int(opcion[0])
    
    if opcion == 1:
        crear_personaje()
    elif opcion == 2:
        editar_personaje()
    elif opcion == 3:
        borrar_personaje()
    else:
        print("Opción incorrecta.")

def gestionar_series():
    system("cls")
    opciones = ['1- Añadir serie', '2- Editar serie', '3- Borrar serie']
    opcion, _ = pick(opciones, '----- Gestionar Series -----', indicator="->")
    opcion = int(opcion[0])
    
    if opcion == 1:
        crear_serie()
    elif opcion == 2:
        editar_serie()
    elif opcion == 3:
        borrar_serie()
    else:
        print("Opción incorrecta.")

def gestionar_estados():
    system("cls")
    opciones = ['1- Añadir estado', '2- Editar estado', '3- Borrar estado']
    opcion, _ = pick(opciones, '----- Gestionar Estados -----', indicator="->")
    opcion = int(opcion[0])
    
    if opcion == 1:
        crear_estado()
    elif opcion == 2:
        editar_estado()
    elif opcion == 3:
        borrar_estado()

def gestionar_generos():
    system("cls")
    opciones = ['1- Añadir género', '2- Editar género', '3- Borrar género']
    opcion, _ = pick(opciones, '----- Gestionar Géneros -----', indicator="->")
    opcion = int(opcion[0])
    
    if opcion == 1:
        crear_sexo()
    elif opcion == 2:
        editar_sexo()
    elif opcion == 3:
        borrar_sexo()

def reportes():
    opciones = ['1- Listar personajes', '2- Listar personajes por signo zodiacal', '3- Listar personajes por mes de cumpleaños', '4- Exportar personajes a mapa', '5- Exportar personaje a HTML', '6- Listar personajes por serie', '7- Listar personajes por estado']
    opcion, _ = pick(opciones, '------- Reportes -------', indicator="->")
    opcion = int(opcion[0])
    
    if opcion == 1:
        listar_personajes()
    elif opcion == 2:
        listar_personajes_por_zodiaco()
    elif opcion == 3:
        listar_personajes_por_mes_de_nacimiento()
    elif opcion == 4:
        exportar_personajes_a_mapa()
    elif opcion == 5:
        exportar_personaje_a_HTML()
    elif opcion == 6:
        listar_personajes_por_serie()
    elif opcion == 7:
        listar_personajes_por_estado()

def configuracion():
    opcion, _ = pick(['1- Gestionar Series', '2- Gestionar Estados', '3- Gestionar Géneros'], '----------- Configuración -----------', indicator="->")
    opcion = int(opcion[0])

    if opcion == 1:
        gestionar_series()
    elif opcion == 2:
        gestionar_estados()
    elif opcion == 3:
        gestionar_generos()

def acerca_de():
    webbrowser.open("https://youtu.be/tTO0a7zM17I")

while True:
    opcion, _ = pick(['1- Gestionar Personajes', '2- Reportes', '3- Configuración', '4- Acerca De', '5- Salir'], '----------- Gestor de Anime -----------', indicator="->")
    opcion = int(opcion[0])

    if opcion == 1:
        gestionar_personajes()
    elif opcion == 2:
        reportes()
    elif opcion == 3:
        configuracion()
    elif opcion == 4:
        acerca_de()
    elif opcion == 5:
        break
    sleep(2)