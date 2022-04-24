class Repositorio:
    def __init__(self, modelo) -> None:
        self.modelo = modelo

    def crear(self, data):
        self.modelo.create(**data)

    def obtener(self):
        return self.modelo.select()
    
    def obtener_por_id(self, id):
        return self.modelo.get_by_id(id)

    def actualizar(self, id, data):
        self.modelo.set_by_id(id, data)

    def borrar(self, id):
        self.modelo.delete_by_id(id)