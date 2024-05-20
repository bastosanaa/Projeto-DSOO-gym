from controllers.controladorProfessor import ControladorProfessor
from models.ficha import Ficha
import random


class ControladorFicha():
    def __init__(self):
        self.__controlador_professor = ControladorProfessor()
        self.__fichas = []

    @property
    def fichas(self):
        return self.__fichas
    
    @property
    def controlador_professor(self):
        return self.__controlador_professor

    def gerar_id_ficha(self):
        return random.randint(1000, 9999)
    
    def criar_ficha(self, descricao, professor, treinos):
        id = self.gerar_id_ficha()
        nova_ficha = Ficha(id, descricao, professor, treinos)
        self.__fichas.append(nova_ficha)

    def excluir_ficha_pelo_id(self, id):
        for ficha in self.__fichas:
            if ficha.id_ficha == id:
                self.__fichas.remove(ficha)
                return ficha
            return None