from views.telaSistema import TelaSistema
from views.telaProfessor import TelaProfessor
from views.telaAluno import TelaAluno
from views.telaFicha import TelaFicha
# from controllers.controladorAluno import ControladorAluno
# from controllers.controladorProfessor import ControladorProfessor
# from controllers.controladorFicha import ControladorFicha

class ControladorSistema:
    def __init__(self):
        # self.__controlador_ficha = ControladorFicha(self)
        # self.__controlador_professor = ControladorProfessor(self)
        # self.__controlador_aluno = ControladorAluno(self)
        self.__tela_sistema = TelaSistema()
        self.__tela_professor = TelaProfessor()
        self.__tela_aluno = TelaAluno()
        self.__tela_ficha = TelaFicha()

    # @property
    # def controlador_ficha(self):
    #     return self.__controlador_ficha
    
    # @property
    # def controlador_professor(self):
    #     return self.__controlador_professor

    # @property
    # def controlador_aluno(self):
    #     return self.__controlador_aluno
    
    def inicializa_sistema(self):
        self.abre_tela()
    
    def cadastra_professor(self):
        self.__tela_professor.mostrar_menu_inicial()

    def cadastra_aluno(self):
        self.__tela_aluno.mostrar_menu_inicial()

    def cadastra_ficha(self):
        self.__tela_ficha.mostrar_menu_inicial()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_professor, 2: self.cadastra_aluno, 3: self.cadastra_ficha}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

