class Endereço():
    def __init__(self, rua: str, complemento: str,
                 bairro: str, cidade: str, cep: str):
        if isinstance(rua, str):
            self.__rua = rua
        if isinstance(complemento, str):
            self.__complemento
        if isinstance(bairro, str):
            self.__bairro = bairro
        if isinstance(cidade, str):
            self.__cidade
        if isinstance(cep, int):
            self.__cep

    @property
    def rua(self):
        return self.__rua

    @property
    def complemento(self):
        return self.__complemento

    @property
    def bairro(self):
        return self.__bairro

    @property
    def cidade(self):
        return self.__cidade

    @property
    def cep(self):
        return self.__cep

    def __str__(self) -> str:
        return 'Rua: ' + self.rua + 'Complemento' + self.complemento
        + 'Bairro: ' + '' + self.bairro + 'Cidade: ' + self.cidade
        + 'Cep:' + self.cep
