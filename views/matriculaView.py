from controllers.matriculaController import ControladorMatricula
from controllers.alunoController import ControladorAluno

class matriculaView():
    def __init__(self):
        self.__controlador_matricula = ControladorMatricula()
        self.__controlador_aluno = ControladorAluno()
    
    def opcoes(self):
        print("OPÇÕES")
        print("1 - Mostrar matrícula")
        print("2 - Realizar nova matricula")
        print("3 - Cancelar matŕicula")    
        opcao = int(input("Escolha a opção: "))
        if opcao == "1":
            self.mostrar_matricula()
        elif opcao == "2":
            pass
    
    def mostrar_matricula(self):
        pass
    
    
    def inserir_plano_matricula(self):
        pass

    def inserir_data_inicio(self):
        pass
    
    def inserir_data_vencimento(self):
        pass
    
    def inserir_data_terminio(self):
        pass
