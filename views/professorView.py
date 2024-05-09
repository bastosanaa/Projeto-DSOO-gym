from controllers.professorController import ControladorProfessor


class TelaProfessor():
    def __init__(self):
        self.__controlador_professor = ControladorProfessor()

    def mostrar_menu_inicial():
        print("OPÇOES")
        print("1.mostrar professores contratados")
        print("2.cadastrar")
        resposta_usuario = input("insira a opção escolhida")
        if resposta_usuario == "1":
            mostrar_professores()
        else:
            pass

    def mostrar_professores(self):
        print(self.__controlador_professor.professores())
        resposta_usuario = input("deseja fazer alterações na lista de professores cadastrados? (s / n)")
        if resposta_usuario == "s":
            mostrar_opcoes_alterecao()
        else:
            voltar_menu = input("deseja voltar ao menu incial? (s / n)")
            if voltar_menu == "s":
                mostrar_menu_inicial()


    def mostrar_opcoes_alterecao():
        print("OPÇOES DE ALTERAÇÃO")
        print("1.cadastrar novo professor")
        print("2.excluir um professor do sistema")
        print("3.alterar professor existente")
        print("4.voltar ao menu inicial")
        resposta_usuario = input("insira a opção escolhida")
        if resposta_usuario == "1":
            cadastrar_professor()
        elif resposta_usuario == "2":
            remover_professor()
        elif resposta_usuario == "3":
            alterar_professor_existente()
        else:
            mostrar_menu_inicial()
        

    def cadastrar_professor(self):
        print("insira as informações de cadastro do professor:")
        nome = input("nome")
        telefone = input("telefone")
        email = input("email")
        turno = input("EXIBIR TURNOS PRE-DEFINIDOS AQUI-SELECT")
        salario = input("salário")
        self.__controlador_professor.cadastrar_professor(nome, telefone, email, turno, salario)
        

    def remover_professor(self):
        print("insira as informações do professor a ser removido:")
        nome = input("nome")
        email = input("email")
        self.__controlador_professor.remover_professor(self, nome, email)
    
    #IMPLEMENTANDO
    def alterar_professor_existente():
        print("que alteração você deseja fazer?")
        print("1.inserir turno na carga horária")
        print("2.remover turno da carga horária")
        resposta_usuario = input("insira a opção escolhida")
    
    def exibir_mensagem_erro(mensagem):
        print(mensagem)
        
