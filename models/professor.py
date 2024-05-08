from pessoa import Pessoa
from turno import Turno


class Professor(Pessoa):
    def __init__(self, nome: str, numero_telefone: int, email: str, cargo: str, turno: str, salario: float):
        super().__init__(nome, numero_telefone, email, cargo, turno)
        self.__salario = salario
        self.__aulas_extras = []
    
    @property
    def salario(self):
        return self.__salario

    @property
    def aulas_extras(self):
        return self.__aulas_extras