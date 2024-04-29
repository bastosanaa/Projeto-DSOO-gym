from funcionario import Funcionario
from treino import Treino


class Professor(Funcionario):
    def __init__(self, nome: str, numero_telefone: int, email: str, cargo: str, turno: str, salario: float):
        super().__init__(nome, numero_telefone, email, cargo, turno, salario)
        self.__aulas_extras = []
    
    @property
    def aulas_extras(self):
        return self.__aulas_extras
    
    def criar_treino(exercicio)
        
        #ACHEI UM BIG PORBLM.... PQ TEMOS UMAS CLASSE TRERINO E 
        #TEM QUE CRIAR O TREINO E DEPOIS CRIAR ESSE METODO
        #AQUELA QUE MONTA O TREINO NOA ENTENDI ESSE CRIAR_TREINO.............. 