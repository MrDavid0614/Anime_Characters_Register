from db import *

class BaseModel(Model):
    id = PrimaryKeyField()
    
    class Meta:
        database = db

class SexoModel(BaseModel):
    descripcion = CharField()

    class Meta:
        db_table = 'Sexo'

class SerieModel(BaseModel):
    nombre = CharField()
    sinopsis = CharField()

    class Meta:
        db_table = 'Serie'

class EstadoModel(BaseModel):
    descripcion = CharField()

    class Meta:
        db_table = 'Estado'

class PersonajeModel(BaseModel):
    nombre = CharField()
    apellido = CharField()
    foto = CharField()
    pronunciacion = CharField()
    serie = ForeignKeyField(SerieModel)
    fecha_nacimiento = CharField()
    poder = CharField()
    frase_favorita = CharField()
    descripcion_vestimenta = CharField()
    edad = IntegerField()
    altura = CharField()
    sexo = ForeignKeyField(SexoModel)
    estado = ForeignKeyField(EstadoModel)
    direccion = CharField()
    latitud = FloatField()
    longitud = FloatField()

    class Meta:
        db_table = 'Personaje'

db.create_tables([SexoModel, SerieModel, EstadoModel, PersonajeModel])