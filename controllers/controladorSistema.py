from views.telaSistema import TelaSistema
from views.telaProfessor import TelaProfessor
from views.telaAluno import TelaAluno
from views.telaFicha import TelaFicha

class ControladorSistema:
    def __init__(self):

        # aqui deve haver a conexao com os controladores e estes chamarao suas respectivas telas para recebimento das entradas do usuario
        self.__tela_sistema = TelaSistema()
        self.__tela_professor = TelaProfessor()
        self.__tela_aluno = TelaAluno()
        self.__tela_ficha = TelaFicha()

    
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

