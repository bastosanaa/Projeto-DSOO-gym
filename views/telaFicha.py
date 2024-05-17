from models.ficha import Ficha
from controllers.controladorFicha import ControladorFicha

class TelaFicha():
    def __init__(self):
        self.__controlador_ficha = ControladorFicha()

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
    
    def pegar_input(self, mensagem):
        return input(mensagem)
        

    def mostrar_menu_inicial(self):
        while True:
            print("-------- Fichas ----------")
            print("1 - mostrar todas as fichas")
            print("2 - cadastrar ficha")
            print("3 - excluir ficha pelo id")
            resposta_usuario = input("Insira a opção escolhida: ")
            if resposta_usuario == "1":
                self.__controlador_ficha.mostrar_fichas()
            elif resposta_usuario == "2":
                pass
            elif resposta_usuario == "3":
                pass
            else:
                print("Opção inválida. Tente novamente.")


    