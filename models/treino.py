from exercicio import Exercicio


class Treino():
    def __init__(self, dia_semana: int, tempo_duracao: int,
                 exercicio: Exercicio):
        if isinstance(dia_semana, int):
            self.__dia_semana = dia_semana
        if isinstance(tempo_duracao, int):
            self.__tempo_duracao = tempo_duracao
        if isinstance(exercicio, Exercicio):
            self.__exercicio = exercicio

    @property
    def dia_semana(self):
        return self.__dia_semana

    @dia_semana.setter
    def dia_semana(self, dia_semana):
        if isinstance(dia_semana, int):
            self.__dia_semana = dia_semana

    @property
    def tempo_duracao(self):
        return self.__tempo_duracao

    @tempo_duracao.setter
    def tempo_duracao(self, tempo_duracao):
        if isinstance(tempo_duracao, int):
            self.__tempo_duracao = tempo_duracao

    @property
    def exercicio(self):
        return self.__exericio

    @exercicio.setter
    def exercicio(self, exercicio):
        if isinstance(exercicio, Exercicio):
            self.__exercicio = exercicio
