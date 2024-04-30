from aparelho import Aparelho


class Exercicio():
    def __init__(self, repeticao: int, serie: int, aparelho: int):
        if isinstance(repeticao, int):
            self.__repeticao = repeticao
        if isinstance(serie, int):
            self.__serie = serie
        if isinstance(aparelho, Aparelho):
            self.__aparelho = aparelho

    @property
    def repeticao(self):
        return self.__repeticao

    @property
    def serie(self):
        return self.__serie

    @property
    def aparelho(self):
        return self.__aparelho

    @repeticao.setter
    def repeticao(self, repeticao):
        if isinstance(repeticao, int):
            self.__repeticao = repeticao

    @serie.setter
    def serie(self, serie):
        if isinstance(serie, int):
            self.__serie = serie

    @aparelho.setter
    def aparelho(self, aparelho):
        if isinstance(aparelho, Aparelho):
            self.__aparelho = aparelho
