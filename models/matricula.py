import random
from plano import Plano


class Matricula():
    def __init__(self, id_matricula: int, plano: Plano, data_inicio: int,
                 mensalidade: float, data_vencimento_pagamento: int,
                 data_termino: int):
        self.__matricula = id_matricula
        if isinstance(plano, Plano):
            self.__plano = plano
        self.__data_inicio = data_inicio
        self.__mesalidade = mensalidade
        self.__data_vencimento_pagamento = data_vencimento_pagamento
        self.__data_termino = data_termino

    @property
    def id_matricula(self):
        return self.__id_matricula
    
    @id_matricula.setter
    def id_matricula(self, id_matricula):
        self.__id_matricula = id_matricula
    