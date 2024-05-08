from models.professor import Professor
from views.professor import ProfessorView

class ControladorProfessor():
    def __init__(self):
        self.__tela_ficha = ProfessorView()
        self.__professores = [Professor]

    @property
    def professores(self):
        return self.__professores


    def definir_salario(self):
        pass
        