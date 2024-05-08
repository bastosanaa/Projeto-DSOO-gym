from controllers.professorController import ControladorProfessor

class TelaProfessor():
    def __init__(self):
        self.__controlador_professor = ControladorProfessor()
        pass

    def cadastrar_professores():
        pass
        #executa crud de cadastro de professor

    def mostrar_professores(self):
        return self.__controlador_professor.professores()
