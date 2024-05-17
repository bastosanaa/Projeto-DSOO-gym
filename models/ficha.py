from models.professor import Professor


class Ficha():
    def __init__(self,id_ficha:int, descricao: str, prof_responsavel: Professor, treinos:list):
        if isinstance(descricao, int):
            self.__descricao = descricao
        if isinstance(prof_responsavel, Professor):
            self.__prof_reponsavel = prof_responsavel
        if isinstance(treinos, list):
            self.__treinos = treinos
        self.__id_ficha = id_ficha
        
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def treinos(self):
        return self.__treinos
    
    @treinos.setter
    def treinos(self, treinos):
        if isinstance(treinos, list):
            self.__treinos = treinos

    @property
    def prof_responsavel(self):
        return self.__prof_reponsavel

    @prof_responsavel.setter
    def prof_responsavel(self, prof_responsavel):
        if isinstance(prof_responsavel, Professor):
            self.__prof_reponsavel = prof_responsavel

    @property
    def id_ficha(self):
        return self.__id_ficha
    
    @id_ficha.setter
    def id_ficha(self, id_ficha):
        self.__id_ficha = id_ficha
