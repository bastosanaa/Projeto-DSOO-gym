from models.turno import Turno
from pessoa import Pessoa
from matricula import Matricula


class Aluno(Pessoa):
    def __init__(self, nome: str, numero_telefone: int,
                 email: str, turno: Turno, matricula: Matricula):
        super().__init__(nome, numero_telefone, email, turno)
        if isinstance(matricula, Matricula):
            self.__matricula = matricula
        self.__fichas = []
