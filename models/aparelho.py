class Aparelho():
    def __init__(self, em_manutenção: bool):
        if isinstance(em_manutenção, bool):
            self.__em_manutenção = em_manutenção

    @property
    def em_manutenção(self):
        self.__em_manutenção
