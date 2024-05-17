from models.pessoa import Pessoa
from models.turno import Turno


class Professor(Pessoa):
    def __init__(self, nome: str, numero_telefone: int, email: str, turno: str, salario: float):
        super().__init__(nome, numero_telefone, email, turno)
        self.__salario = salario
        self.__aulas_extras = []
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
