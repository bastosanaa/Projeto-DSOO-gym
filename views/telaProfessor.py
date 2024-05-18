from controllers.controladorProfessor import ControladorProfessor


class TelaProfessor():
    def __init__(self):
        self.__controlador_professor = ControladorProfessor(self)

    def mostrar_menu_inicial(self):
        while True:
            print()
            print("--------- Professores ----------")
            print("1 - mostrar professores contratados")
            print("2 - cadastrar")
            resposta_usuario = input("Insira a opção escolhida: ")
            if resposta_usuario == "1":
                self.mostrar_professores()
            elif resposta_usuario == "2":
                self.cadastrar_professor()
            else:
                print("Opção inválida. Tente novamente.")

    def mostrar_professores(self):
        print()
        if self.__controlador_professor.professores:
            n_prof = 1
            for professor in self.__controlador_professor.professores:
                print(f'{n_prof} - {professor.nome}')
                n_prof += 1
        else:
            print("Ainda não existem professores cadastrados")
        resposta_usuario = input("deseja fazer alterações na lista de professores cadastrados? (s / n)")
        if resposta_usuario == "s":
            self.mostrar_opcoes_alterecao()
        else:
            voltar_menu = input("deseja voltar ao menu incial? (s / n)")
            if voltar_menu == "s":
                self.mostrar_menu_inicial()


    def mostrar_opcoes_alterecao(self):
        print()
        while True:
            print("--------- Professores ----------")
            print("Opções de alteração")
            print("1 - cadastrar novo professor")
            print("2 - excluir um professor do sistema")
            print("3 - alterar turno de um professor cadastrado")
            print("4 - voltar ao menu inicial")
            resposta_usuario = input("Insira a opção escolhida: ")
            if resposta_usuario == "1":
                self.cadastrar_professor()
            elif resposta_usuario == "2":
                self.remover_professor()
            elif resposta_usuario == "3":
                self.alterar_turno()
            elif resposta_usuario == "4":
                return
            else:
                print("Opção inválida. Tente novamente.")

    def cadastrar_professor(self):
        print()
        print("insira as informações de cadastro do professor:")
        nome = input("nome: ")
        telefone = input("telefone: ")
        email = input("email: ")
        turno = input("EXIBIR TURNOS PRE-DEFINIDOS AQUI-SELECT")
        salario = input("salário: ")
        prof_cadastrado = self.__controlador_professor.cadastrar_professor(nome, telefone, email, turno, salario)
        if prof_cadastrado:
            print(f'Professor(a) {nome} cadastrado com sucesso!')
        else: 
            print("Este professor já está cadastrado")
        self.mostrar_menu_inicial()
        

    def remover_professor(self):
        print()
        print("insira as informações do professor a ser removido:")
        nome = input("nome: ")
        email = input("email: ")
        professor_removido = self.__controlador_professor.remover_professor(nome, email)
        if professor_removido:
            print(f'Professor {nome} removido com sucesso!')
        else:
            print("professor nao encontrado")
        self.mostrar_menu_inicial()
    
    #IMPLEMENTANDO
    def alterar_turno(self):
        print()
        prof_cadastrado = None
        while not prof_cadastrado:
            prof_input = input("Insira o nome de um professor para alterar turnos: ")
            prof_cadastrado = self.__controlador_professor.acessar_professor_pelo_nome(prof_input)
            if not prof_cadastrado:
                print("Professor nao encontrado")
        print(f'O turno atual de {prof_cadastrado} é {prof_cadastrado.turno}')
        continuar = input("continuar alteração de turno? (s / n)")
        if continuar == "s":
            turno = self.selecionar_turno()
            self.__controlador_professor.alterar_turno(prof_cadastrado,turno)
            print(f'O turno atual de {prof_cadastrado} é {prof_cadastrado.turno}')
        self.mostrar_menu_inicial()

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def selecionar_turno(self):
        print("1 - matutino")
        print("2 - vespertino")
        print("3 - noturno")
        turno = input("Digite o código do turno escolhido: ")
        return self.__controlador_professor.escolher_turno(turno)

        
