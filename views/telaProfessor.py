from simple_chalk import chalk, cyan, red, green, bold
from controllers.controladorProfessor import ControladorProfessor
from views.telaSistema import TelaSistema
from telaAbstrata import TelaAbstrata


class TelaProfessor(TelaAbstrata):
    def __init__(self):
        self.__controlador_professor = ControladorProfessor()
        self.__tela_sistema = TelaSistema()



    def mostrar_menu_inicial(self):
        while True:
            print()
            print(chalk.cyan.bold("----------- Professores ------------"))
            print("1 - Mostrar professores cadastrados")
            print("2 - Cadastrar novo professor")
            print("3 - Alterar professor já cadastrado")
            print("4 - Vizualizar professor já cadastrado")
            print("5 - Relatório de professores por turno")
            print("0 - Voltar ao menu inicial")
            resposta_usuario = input(chalk.bold("Insira a opção escolhida: "))
            print(chalk.cyan.bold("-------------------------------------"))
            if resposta_usuario == "1":
                self.mostrar_professores()
            elif resposta_usuario == "2":
                self.cadastrar_professor()
            elif resposta_usuario == "3":
                self.mostrar_opcoes_alterecao()
            elif resposta_usuario == "4":
                self.visualizar_professor()
            elif resposta_usuario == "5":
                self.calcular_professores_por_turno()
            elif resposta_usuario == "0":
                break
            else:
                print()
                print(chalk.red("Opção inválida. Tente novamente. ❌"))

    def mostrar_professores(self):
        print()
        if self.__controlador_professor.professores:
            n_prof = 1
            for professor in self.__controlador_professor.professores:
                print(f'{n_prof} - {professor.nome}')
                n_prof += 1
        else:
            print(chalk.bold("Ainda não existem professores cadastrados"))
            self.mostrar_menu_inicial()


    def mostrar_opcoes_alterecao(self):
        print()
        if self.__controlador_professor.professores:
            while True:
                print(chalk.cyan.bold("----------- Professores ------------"))
                print(chalk.bold("Opções de alteração"))
                print("1 - cadastrar novo professor")
                print("2 - excluir um professor do sistema")
                print("3 - alterar turno de um professor cadastrado")
                print("4 - voltar ao menu inicial")
                resposta_usuario = input(chalk.bold("Insira a opção escolhida: "))
                print(chalk.cyan.bold("-------------------------------------"))
                if resposta_usuario == "1":
                    self.cadastrar_professor()
                elif resposta_usuario == "2":
                    self.remover_professor()
                elif resposta_usuario == "3":
                    self.alterar_turno()
                elif resposta_usuario == "4":
                    self.mostrar_menu_inicial()
                else:
                    print()
                    print(chalk.red("Opção inválida. Tente novamente. ❌"))
                    print()
        else: 
            print(chalk.bold("Nenhum professor cadastrado"))

    def cadastrar_professor(self):
        print()
        print(chalk.bold("Insira as informações de cadastro do professor:"))
        while True:
            try:
                nome = str(input("Nome: "))
                telefone = int(input("telefone (ex:DD999999999): "))
                email = str(input("email (ex:nome@bodylab.com): "))
                turno = self.selecionar_turno()
                salario = int(input("salário: "))
                prof_cadastrado = self.__controlador_professor.cadastrar_professor(nome, telefone, email, turno, salario)
                break
            except ValueError:
                print(chalk.red("Valor inserido é inválido, tente novamente: ❌"))
        if prof_cadastrado:
            print(chalk.green(f'Professor(a) {nome} cadastrado com sucesso! ✅'))
            exit()
        else:
            print(chalk.bold("Este professor já está cadastrado"))
        
        

    def remover_professor(self):
        print()
        print(chalk.bold("Insira as informações do professor a ser removido:"))
        nome = input("Nome: ")
        email = input("Email: ")
        professor_removido = self.__controlador_professor.remover_professor(nome, email)
        if professor_removido:
            print(chalk.green(f'Professor {nome} removido com sucesso! ✅'))
        else:
            print(chalk.red("Professor não encontrado ❌"))
        self.mostrar_menu_inicial()
    
    def alterar_turno(self):
        print()
        prof_cadastrado = None
        while not prof_cadastrado:
            prof_input = input(chalk.bold("Insira o nome de um professor para alterar turnos: "))
            prof_cadastrado = self.__controlador_professor.acessar_professor_pelo_nome(prof_input)
            if not prof_cadastrado:
                print(chalk.red("Professor nao encontrado ❌"))
        print(f'O turno atual de {prof_cadastrado.nome} é {prof_cadastrado.turno}')
        continuar = input("continuar alteração de turno? (s / n)")
        if continuar == "s":
            turno = self.selecionar_turno()
            self.__controlador_professor.alterar_turno(prof_cadastrado,turno)
            print(chalk.green("Professor alterado com sucesso! ✅"))
            print(f'O turno atual de {prof_cadastrado.nome} é {prof_cadastrado.turno}')
        self.mostrar_menu_inicial()

    def selecionar_turno(self):
        print()
        print(chalk.bold("--- Turnos ---"))
        print("1 - matutino")
        print("2 - vespertino")
        print("3 - noturno")
        turno = int(input(chalk.bold("Digite o código do turno escolhido: ")))
        if turno in [1,2,3]:
            return self.__controlador_professor.escolher_turno((turno))
        raise ValueError
    
    def visualizar_professor(self):
        nome_professor = input("Qual professor você deseja visualizar: ")
        professor = self.__controlador_professor.acessar_professor_pelo_nome(nome_professor)
        print()
        if professor:
            print(chalk.cyan.bold("------- Informações do professor -------"))
            print(f'Nome: {professor.nome}')
            print(f'Email: {professor.email}')
            print(f'Telefone: {professor.numero_telefone}')
            print(f'Salário: {professor.salario}')
            print(f'Turno: {professor.turno}')
            print(chalk.cyan.bold("----------------------------------------"))
        else:
            print(chalk.red("Professor nao encontrado ❌"))
            self.mostrar_menu_inicial()

    def calcular_professores_por_turno(self):
        matutino, vespertino, noturno = self.__controlador_professor.calcular_professores_por_turno()
        print()
        print(chalk.cyan.bold("------- Professores por turno -------"))
        print(f'{matutino} professores trabalham no turno matutino')
        print(f'{vespertino} professores trabalham no turno vespertino')
        print(f'{noturno} professores trabalham no turno noturno')
        print(chalk.cyan.bold("--------------------------------------"))
