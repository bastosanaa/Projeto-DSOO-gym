from pessoa import Pessoa
from abc import ABC, abstractmethod

class Funcionario(Pessoa, ABC):
    @abstractmethod
    def __init__(self, nome: str, numero_telefone: int, email: str, cargo:str, turno:str, salario: float):
        super().__init__(nome, numero_telefone, email)
        if isinstance(turno, str):
            self.__turno = turno
        if isinstance(cargo, str):
            self.__cargo = cargo
        if isinstance(salario, float):
            self.__salario = salario
        
    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo):
        if isinstance(cargo, str):
            self.__cargo = cargo 
    
    @property
    def turno(self):
        return self.__turno
    
    @turno.setter
    def turno(self, turno):
        if isinstance(turno, str):
            self.__turno = turno
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        if isinstance (salario, float):
            self.__salario = salario
    
    