from models.pessoa import Pessoa
from models.turno import Turno


class Professor(Pessoa):
    def __init__(self, nome: str, numero_telefone: int, email: str, turno: Turno, salario: float):
        super().__init__(nome, numero_telefone, email, turno)
        self.__salario = salario
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        if isinstance(salario, int):
            self.__salario = salario
