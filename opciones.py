from pyclbr import Function
from modelos import PersonajeModel, SerieModel, EstadoModel, SexoModel
from repositorio import Repositorio
from pick import pick
from os import system
from time import sleep
from folium import Map, Marker
from pathlib import Path
import requests
import webbrowser

repositorio_personaje = Repositorio(PersonajeModel)
repositorio_serie = Repositorio(SerieModel)
repositorio_estado = Repositorio(EstadoModel)
repositorio_sexo = Repositorio(SexoModel)

def crear_personaje():
    system("cls")
    generos_registros = repositorio_sexo.obtener()
    series_registros = repositorio_serie.obtener()
    series = []
    generos = []

    if len(series_registros) > 0 and len(generos_registros) > 0:
        for serie in series_registros:
            series.append(serie.nombre)

        for genero in generos_registros:
            generos.append(genero.descripcion)

        nombre = input("Ingrese el nombre del personaje: ")
        apellido = input("Ingrese el apellido del personaje: ")
        foto = input("Ingrese una url con la foto del personaje: ")
        pronunciacion = input("Ingrese la pronunciación del nombre del personaje:")
        system("cls")
        serie, _ = pick(series, '----- Seleccionar serie a la que pertenece -----', indicator="->")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del personaje: (DD/MM) ")
        poder = input("Descripción sobre el poder del personaje: ")
        frase = input("Ingrese la frase favorita del personaje: ")
        vestimenta = input("Descripción de la vestimenta del personaje: ")
        edad = int(input("Ingrese la edad del personaje: "))
        altura = input("Ingrese la altura del personaje:")
        system("cls")
        sexo, _ = pick(generos, '----- Seleccionar sexo del personaje -----', indicator="->")
        estado, _ = pick(['Vivo', 'Muerto', 'Indefinido'], '----- Seleccionar estado del personaje -----', indicator="->")
        direccion = input("Ingrese la dirección del personaje: ")
        coordenadas = input("Ingrese las coordenadas de la ubicación del personaje: ")

        if coordenadas == "":
            coordenadas = "18.707079338453887, -70.60260770253315"

        latitud, longitud = coordenadas.split(", ")

        serie = SerieModel.select().where(SerieModel.nombre == serie )
        sexo = SexoModel.select().where(SexoModel.descripcion == sexo)
        estado = EstadoModel.select().where(EstadoModel.descripcion == estado)
        repositorio_personaje.crear({ 'nombre': nombre, 'apellido': apellido, 'foto': foto, 'pronunciacion': pronunciacion, 'serie_id': serie, 'fecha_nacimiento': fecha_nacimiento, 'poder': poder, 'frase_favorita': frase, 'descripcion_vestimenta': vestimenta, 'edad': edad, 'altura': altura, 'sexo_id': sexo, 'estado_id': estado, 'direccion': direccion, 'latitud': float(latitud), 'longitud': float(longitud) })
        print("El personaje se ha creado exitósamente")
    else:
        print("Necesitas configurar tus estados, géneros y series antes de añadir un personaje...")
    sleep(1.5)

def editar_personaje():
    system("cls")
    personaje_id = input("Ingrese el id del personaje que desea editar: ")

    personaje = repositorio_personaje.obtener_por_id(personaje_id)

    generos_registros = repositorio_sexo.obtener()
    series_registros = repositorio_serie.obtener()
    series = []
    generos = []
    for serie in series_registros:
        series.append(serie.nombre)

    for genero in generos_registros:
        generos.append(genero.descripcion)

    nombre = input("Ingrese el nombre del personaje: ")
    apellido = input("Ingrese el apellido del personaje: ")
    foto = input("Ingrese una url con la foto del personaje: ")
    pronunciacion = input("Ingrese la pronunciación del nombre del personaje: \n\n")
    serie, _ = pick(series, '----- Seleccionar serie a la que pertenece -----', indicator="->")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del personaje: ")
    poder = input("Descripción sobre el poder del personaje: ")
    frase = input("Ingrese la frase favorita del personaje: ")
    vestimenta = input("Descripción de la vestimenta del personaje: ")
    edad = int(input("Ingrese la edad del personaje: "))
    altura = input("Ingrese la altura del personaje: \n\n")
    sexo, _ = pick(generos, '----- Seleccionar sexo del personaje -----', indicator="->")
    estado, _ = pick(['Vivo', 'Muerto', 'Indefinido'], '----- Seleccionar estado del personaje -----', indicator="->")
    direccion = input("Ingrese la dirección del personaje: ")
    coordenadas = input("Ingrese las coordenadas de la ubicación del personaje: ")

    if coordenadas == "":
        coordenadas = "18.707079338453887, -70.60260770253315"

    latitud, longitud = coordenadas.split(", ")

    serie = SerieModel.select().where(SerieModel.nombre == serie )
    sexo = SexoModel.select().where(SexoModel.descripcion == sexo)
    estado = EstadoModel.select().where(EstadoModel.descripcion == estado)

    personaje.nombre = nombre
    personaje.apellido = apellido
    personaje.foto = foto
    personaje.pronunciacion = pronunciacion
    personaje.serie_id = serie
    personaje.fecha_nacimiento = fecha_nacimiento
    personaje.poder = poder
    personaje.frase_favorita = frase
    personaje.descripcion_vestimenta = vestimenta
    personaje.edad = edad
    personaje.altura = altura
    personaje.sexo_id = sexo
    personaje.estado_id = estado
    personaje.direccion = direccion
    personaje.latitud = latitud
    personaje.longitud = longitud
    personaje.save()

    print("El personaje se actualizó correctamente")
    sleep(1.2)

def borrar_personaje():
    personaje_id = input("Ingrese el id del personaje que desea borrar: ")
    repositorio_personaje.borrar(personaje_id)

    print("El personaje se borró exitosamente")
    sleep(1.2)

def crear_serie():
    nombre = input("Ingrese el nombre de la serie: ")
    sinopsis = input("Ingrese la sinopsis de la serie: ")

    repositorio_serie.crear({ 'nombre': nombre, 'sinopsis': sinopsis })
    print("La serie se ha creado exitósamente")
    sleep(1.2)

def editar_serie():
    serie_id = input("Ingrese el id de la serie que desea actualizar: ")

    serie = repositorio_serie.obtener_por_id(serie_id)
    serie.nombre = input("Ingrese el nombre de la serie: ")
    serie.sinopsis = input("Ingrese la sinopsis de la serie: ")
    serie.save()

    print("La serie se actualizó correctamente")
    sleep(1.2)

def borrar_serie():
    serie_id = input("Ingrese el id de la serie a eliminar: ")

    repositorio_serie.borrar(serie_id)
    print("La serie se borró exitosamente")
    sleep(1.2)

def crear_sexo():
    descripcion = input("Ingrese el género a añadir: ")
    repositorio_sexo.crear({ 'descripcion': descripcion })
    print("El sexo se ha creado exitósamente")
    sleep(1.2)

def editar_sexo():
    sexo_id = input("Ingrese el id del género a editar: ")
    
    sexo = repositorio_sexo.obtener_por_id(sexo_id)
    sexo.descripcion = input("Ingrese el género a añadir: ")
    sexo.save()

    print("El género se actualizó correctamente")
    sleep(1.2)

def borrar_sexo():
    sexo_id = input("Ingrese el id del género a eliminar: ")
    repositorio_sexo.borrar(sexo_id)

    print("El género se borró exitosamente")
    sleep(1.2)

def crear_estado():
    descripcion = input("Ingrese el estado a añadir: ")
    repositorio_estado.crear({ 'descripcion': descripcion })
    print("El estado se ha creado exitósamente")
    sleep(1.2)

def editar_estado():
    estado_id = input("Ingrese el id del estado a editar: ")

    estado = repositorio_estado.obtener_por_id(estado_id)
    estado.descripcion = input("Ingrese el estado a añadir: ")
    estado.save()
    print("El estado se actualizó exitósamente")
    sleep(1.2)

def borrar_estado():
    estado_id = input("Ingrese el id del estado a eliminar: ")
    repositorio_estado.borrar(estado_id)

    print("El estado se eliminó correctamente")
    sleep(1.2)

def listar_personajes():
    system("cls")
    print("------- Lista de personajes -------\n")
    personajes = repositorio_personaje.obtener()
    print(f"Nombre \t\t\t Apellido \t\t\t Serie \t\t\t Género \t\t\t Edad")
    for personaje in personajes:
        serie = repositorio_serie.obtener_por_id(personaje.serie_id)
        sexo = repositorio_sexo.obtener_por_id(personaje.sexo_id)
        print(f"{personaje.nombre} \t\t\t {personaje.apellido} \t\t\t {serie.nombre} \t\t {sexo.descripcion} \t\t\t {personaje.edad}")
    
    sleep(3)

def listar_personajes_por_zodiaco():
    system("cls")
    print("------- Personajes por zodiaco -------\n")
    personajes = repositorio_personaje.obtener()
    personajes_por_zodiaco = {}

    for personaje in personajes:
        dia, mes = personaje.fecha_nacimiento.split("/")
        res = requests.get(f"https://zodiacal-api.herokuapp.com/?dia={dia}&mes={mes}").json()
        signo = res['signo']
        
        if personajes_por_zodiaco.get(signo):
            personajes_por_zodiaco[signo].append(personaje)
        else:
            personajes_por_zodiaco[signo] = [personaje]
    
    signos = list(personajes_por_zodiaco.keys())
    signos.sort()

    for signo in signos:
        print(f"\n---- Signo {signo}:\n")
        for personaje in personajes_por_zodiaco.get(signo):
            print(f"\t {personaje.nombre} {personaje.apellido}")

    sleep(5)

def listar_personajes_por_mes_de_nacimiento():
    system("cls")
    print("------- Personajes por mes de nacimiento -------\n")
    personajes = repositorio_personaje.obtener()
    personajes_por_mes = {}

    for personaje in personajes:
        mes = int(personaje.fecha_nacimiento.split("/")[1])

        if personajes_por_mes.get(mes):
            personajes_por_mes[mes].append(personaje)
        else:
            personajes_por_mes[mes] = [personaje]
    meses = list(personajes_por_mes.keys())
    meses.sort()

    for mes in meses:
        print(f"\n---- Mes {mes}:\n")
        for personaje in personajes_por_mes.get(mes):
            print(f"\t {personaje.nombre} {personaje.apellido}")

    sleep(5)

def listar_personajes_por_serie():
    series = repositorio_serie.obtener()
    
    for serie in series:
        cantidad_personajes = len(PersonajeModel.select().where(PersonajeModel.serie == serie.id))
        print(f"---------- {serie.nombre} ----------")
        
        if cantidad_personajes < 1:
            print(f"{serie.nombre} no tiene personajes.\n")
        else:
            print(f"{serie.nombre} tiene {cantidad_personajes}", "personajes." if cantidad_personajes > 1 else "personaje.", "\n")

    sleep(2)

def listar_personajes_por_estado():
    estados = repositorio_estado.obtener()
    
    for estado in estados:
        cantidad_personajes = len(PersonajeModel.select().where(PersonajeModel.estado == estado.id))
        print(f"---------- {estado.descripcion} ----------")
        
        if cantidad_personajes < 1:
            print(f"No hay ningún personaje {estado.descripcion}.\n")
        else:
            print(f"Hay {cantidad_personajes}", "personajes" if cantidad_personajes > 1 else "personaje", "{}".format(f"{estado.descripcion}s." if cantidad_personajes > 1 else f"{estado.descripcion}."), "\n")

        sleep(2)

def exportar_personajes_a_mapa():
    personajes = repositorio_personaje.obtener()

    mapa = Map([50.418041, 30.514424], zoom_start=1)

    for personaje in personajes:
        serie = repositorio_serie.obtener_por_id(personaje.serie_id)
        Marker(location=[personaje.latitud, personaje.longitud], popup=f"<p><strong>Nombre:</strong><br>{personaje.nombre} {personaje.apellido}</p><p><strong>Edad:</strong><br>{personaje.edad}</p><p><strong>Serie:</strong><br>{serie.nombre}</p>", tooltip=f"Personaje de {serie.nombre}").add_to(mapa)

    mapa.save("mapa.html")
    webbrowser.open(f"file:///{Path().resolve()}/mapa.html")

def exportar_personaje_a_HTML():
    personaje_id = input("Ingre el id del personaje que desea exportar: ")

    personaje = repositorio_personaje.obtener_por_id(personaje_id)
    serie = repositorio_serie.obtener_por_id(personaje.serie_id)
    sexo = repositorio_sexo.obtener_por_id(personaje.sexo_id)
    estado = repositorio_estado.obtener_por_id(personaje.estado_id)
    estado_clase_css = 'text_muted'
    
    if estado.descripcion == 'Vivo':
        estado_clase_css = 'alive'
    elif estado.descripcion == 'Muerto':
        estado_clase_css = 'dead'

    css = open("./styles.css", "w")
    css.write("""
    main {
            height: 100vh;
            outline: 3px solid black;
            display: flex;
            justify-content: space-evenly;
            font-family: sans-serif;
        }

        img {
            width: 650px;
            height: 650px;
            object-fit: contain;
        }

        .image-container {
            padding-left: 80px;
            display: flex;
            align-items: start;
            width: 100%;
        }

        .info-container{
            width: 100%;
        }

        h1 {
            text-align: center;
        }

        p {
            font-size: 1.2rem;
            font-weight: bold;
        }

        span {
            font-weight: normal;
        }

        .text-muted {
            color: gray;
            font-size: 1.1rem;
        }

        .alive {
            color: green;
        }

        .dead {
            color: red;
        }
    """)
    css.close()
    html = open("./index.html", "w", encoding="utf-8")
    html.write(f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{personaje.nombre}</title>
    <link rel="stylesheet" href="./styles.css">
</head>
<body>
    <main>
        <div class="image-container">
            <img src="{personaje.foto}" alt="Foto de {personaje.nombre}">
        </div>
        <div class="info-container">
            <h1>{personaje.nombre} {personaje.apellido} <span class="text-muted">({serie.nombre})</span></h1>
            <p>Pronunciación: <span>{personaje.pronunciacion}</span></p>
            <p>Fecha de nacimiento: <span>{personaje.fecha_nacimiento}</span></p>
            <p>Edad: <span>{personaje.edad}</span></p>
            <p>Poder: <span>{personaje.poder}</span></p>
            <p>Frase favorita: <span>{personaje.frase_favorita}</span></p>
            <p>Descripción de su vestimenta: <span>{personaje.descripcion_vestimenta}</span></p>
            <p>Sexo: <span>{sexo.descripcion}</span></p>
            <p>Estado: <span class="{estado_clase_css}">{estado.descripcion}</span></p>
            <p>Dirección: <span>{personaje.direccion}</span></p>
        </div>
    </main>
</body>
</html>
    """)
    html.close()
    webbrowser.open(f"file:///{Path().resolve()}/index.html")