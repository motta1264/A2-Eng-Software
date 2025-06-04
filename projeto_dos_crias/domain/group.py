class Group:
    def __init__(self, id, nome, descricao, materia, estilo, administrador_id):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.materia = materia
        self.estilo = estilo  # "virtual" ou "presencial"
        self.administrador_id = administrador_id
