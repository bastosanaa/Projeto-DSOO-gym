from controllers.controladorProfessor import ControladorProfessor
from models.ficha import Ficha
import random


class ControladorFicha():
    def __init__(self,controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_professor = ControladorProfessor(controlador_sistema)
        self.__fichas = []

    @property
    def fichas(self):
        return self.__fichas

    def gerar_id_ficha(self):
        return random.randint(1000, 9999)
    
    # def criar_ficha(self):
    #     id = self.gerar_id_ficha()
    #     descricao = self.__tela_ficha.pegar_input("Descreva a ficha a criar: ")
    #     professor = None
    #     treinos = []
        
    #     while not professor:
    #         nome_professor = self.__tela_ficha.pegar_input("Escolha um professor pelo nome: ")
    #         professor = self.__controlador_professor.acessar_professor_pelo_nome(nome_professor)
    #         professor = self.__controlador_sistema.controlador_professor.acessar_professor_pelo_nome(nome_professor)
    #         if not professor:
    #             self.__tela_ficha.mostrar_mensagem("Professor não encontrado, tente novamente.")
        
    #     n_treinos = int(self.__tela_ficha.pegar_input("Quantos treinos terá a ficha? "))
    #     for _ in range(n_treinos):
    #         treino = self.__tela_ficha.pegar_input("Insira o(s) grupo(s) muscular do treino: ")
    #         treinos.append(treino)
        
    #     nova_ficha = Ficha(id, descricao, professor, treinos)
    #     self.__fichas.append(nova_ficha)
    #     self.__tela_ficha.mostrar_mensagem(f'Ficha {id} criada com sucesso!')

    # def excluir_ficha_pelo_id(self, id):
    #     for ficha in self.__fichas:
    #         if ficha.id_ficha == id:
    #             self.__fichas.remove(ficha)
    #             self.__tela_ficha.mostrar_mensagem(f'Ficha {id} removida com sucesso!')
    #             return ficha
    #     self.__tela_ficha.mostrar_mensagem(f'Ficha {id} não encontrada')
        # return None
