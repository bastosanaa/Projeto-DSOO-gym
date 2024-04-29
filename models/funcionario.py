from pessoa import Pessoa
from abc import ABC, abstractmethod

class Funcionario(Pessoa, ABC):
    @abstractmethod
    def __init__(self, nome: str, numero_telefone: int, email: str, cargo, turno, salario: int):
        super().__init__(nome, numero_telefone, email)
        if isinstance(sala)
