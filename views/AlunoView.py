from ficha import Ficha

class AlunoView():
    def mostra_opcoes(self):
        print("-------- Aluno ----------")
        print("01 - Listar treinos Ficha")
        print("02 - Visualizar matricula")
        print("03 - Abrir pedido de cancelamento de matricula")
        opçao = int(input("Escolha a opção: "))
        return opçao
    
    def lista_treinos_ficha(self, ficha:Ficha):
        
        
        