from controllers.professorController import ControladorProfessor


class TelaProfessor():
    def __init__(self):
        self.__controlador_professor = ControladorProfessor()

    def mostrar_menu_inicial(self):
        print("OPÇOES")
        print("1.mostrar professores contratados")
        print("2.cadastrar")
        resposta_usuario = input("insira a opção escolhida")
        if resposta_usuario == "1":
            self.mostrar_professores()
        else:
            pass

    def mostrar_professores(self):
        print(self.__controlador_professor.professores)
        resposta_usuario = input("deseja fazer alterações na lista de professores cadastrados? (s / n)")
        if resposta_usuario == "s":
            self.mostrar_opcoes_alterecao()
        else:
            voltar_menu = input("deseja voltar ao menu incial? (s / n)")
            if voltar_menu == "s":
                self.mostrar_menu_inicial()


    def mostrar_opcoes_alterecao(self):
        print("OPÇOES DE ALTERAÇÃO")
        print("1.cadastrar novo professor")
        print("2.excluir um professor do sistema")
        print("3.alterar professor existente")
        print("4.voltar ao menu inicial")
        resposta_usuario = input("insira a opção escolhida")
        if resposta_usuario == "1":
            self.cadastrar_professor()
        elif resposta_usuario == "2":
            self.remover_professor()
        elif resposta_usuario == "3":
            self.alterar_professor_existente()
        else:
            self.mostrar_menu_inicial()
        

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
        self.__controlador_professor.remover_professor(nome, email)
    
    #IMPLEMENTANDO
    def alterar_professor_existente(self):
        print("que alteração você deseja fazer?")
        print("1.inserir turno na carga horária")
        print("2.remover turno da carga horária")
        resposta_usuario = input("insira a opção escolhida")
        prof_cadastrado = None
        if resposta_usuario == "1":
            while not prof_cadastrado:
                prof_input = input("Selecione um professor para alterar turnos")
                prof_cadastrado = self.__controlador_professor.acessar_professor_pelo_nome(prof_input)
                # while professor.turnos == 2 -> erro
                # select turno
                self.__controlador_professor.adicionar_turno_professor
        if resposta_usuario == "2":
            while not prof_cadastrado:
                prof_input = input("Selecione um professor para alterar turnos")
                self.__controlador_professor.acessar_professor_pelo_nome(prof_input)
    

    def exibir_mensagem_erro(self, mensagem):
        print(mensagem)
        
