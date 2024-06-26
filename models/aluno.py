from models.turno import Turno
from models.pessoa import Pessoa
from models.matricula import Matricula


class Aluno(Pessoa):
    def __init__(self, nome: str, numero_telefone: int,
                 email: str, turno: Turno, matricula: Matricula):
        super().__init__(nome, numero_telefone, email, turno)
        if isinstance(matricula, Matricula):
            self.__matricula = matricula
        self.__ficha = ''

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, Matricula):
            self.__matricula = matricula

    @property
    def ficha(self):
        return self.__ficha
