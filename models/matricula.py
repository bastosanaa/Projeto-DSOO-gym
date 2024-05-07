from plano import Plano


class Matricula():
    def __init__(self, id_matricula: int, plano: Plano, data_inicio: int,
                 mensalidade: float, data_vencimento_pagamento: int,
                 data_termino: int):
        self.__matricula = id_matricula
        if isinstance(plano, Plano):
            self.__plano = plano
        self.__data_inicio = data_inicio
        self.__mensalidade = mensalidade
        self.__data_vencimento_pagamento = data_vencimento_pagamento
        self.__data_termino = data_termino

    @property
    def id_matricula(self):
        return self.__id_matricula

    @id_matricula.setter
    def id_matricula(self, id_matricula):
        self.__id_matricula = id_matricula

    @property
    def plano(self):
        return self.__plano

    @plano.setter
    def plano(self, plano):
        if isinstance(plano, Plano):
            self.__plano = plano

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio):
        self.__data_inicio = data_inicio

    @property
    def mensalidade(self):
        return self.__mensalidade

    @mensalidade.setter
    def mensalidade(self, mensalidade):
        self.__mensalidade = mensalidade

    @property
    def data_vencimento_pagamento(self):
        return self.__data_vencimento_pagamento

    @data_vencimento_pagamento.setter
    def data_vencimento_pagamento(self, data_vencimento_pagamento):
        self.__data_vencimento_pagamento = data_vencimento_pagamento

    @property
    def data_termino(self):
        return self.__data_termino

    @data_termino.setter
    def data_termino(self, data_termino):
        self.__data_termino = data_termino
