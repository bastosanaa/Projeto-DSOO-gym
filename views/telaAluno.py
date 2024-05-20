from simple_chalk import chalk, magenta, bold
from models.aluno import Aluno
from controllers.controladorAluno import ControladorAluno
from models.plano import Plano
from views.telaSistema import TelaSistema



class TelaAluno():
    def __init__(self):
        self.__controlador_aluno = ControladorAluno(self)
        self.__tela_sistema = TelaSistema()

    def mostrar_menu_inicial(self):
        print()
        print("-------- Aluno ----------")
        print("Escolha a opção:")
        print("1 - Assuntos relacionados à matricula")
        print("2 - Assuntos relacionados à ficha")
        print("3 - Gerar relatórios")
        print("4 - Listar alunos")
        print("5 - Voltar para o menu inicial")
        print("0 - Sair")

        opcao = int(input("Escolha a opção: "))

        if opcao == 1:
            self.assuntos_relacionados_a_matricula()
        elif opcao == 2:
            self.assuntos_relacionados_a_ficha()
        elif opcao == 3:
            self.gerar_relatorios()
        elif opcao == 4:
            self.listar_alunos()
        elif opcao == 5:
            self.__tela_sistema.tela_opcoes()
        elif opcao == 0:
            exit(0)
        else:
            print("Opção inválida. Tente novamente.")
            self.mostrar_menu_inicial()

    def assuntos_relacionados_a_matricula(self):
        print()
        print("-------- Matrícula ----------")
        print("Escolha a opção:")
        print("1 - Realizar matrícula")
        print("2 - Cancelar matrícula")
        print("3 - Mostrar dados da matrícula")
        print("4 - Alterar algum dado da matrícula")
        print("0 - retornar")
        opcao = int(input("Escolha a opção: "))
        if opcao == 1:
            self.realizar_matricula()
        elif opcao == 2:
            self.cancelar_matricula()
        elif opcao == 3:
            self.mostrar_dados_matricula()
        elif opcao == 4:
            self.alterar_dado_matricula()
        elif opcao == 0:
            self.mostrar_menu_inicial()
        else:
            print("Opção inválida. Tente novamente.")
            self.assuntos_relacionados_a_matricula()

    def assuntos_relacionados_a_ficha(self):
        print()
        print("-------- Ficha ----------")
        print("Escolha a opção:")
        print("1 - Mostrar treinos da ficha")
        print("0 - retornar")

        opcao = int(input("Escolha a opção: "))

        if opcao == 1:
            self.mostrar_dados_ficha()
        elif opcao == 0:
            self.mostrar_menu_inicial()
        else:
            print("Opção inválida. Tente novamente.")
            self.assuntos_relacionados_a_ficha()

    def realizar_matricula(self):
        print()
        nome_aluno = input("Digite o nome do aluno: ")
        numero_telefone = int(input("Digite o número de telefone do aluno (ex:DD999999999): "))
        email = input("Digite o email do aluno (ex:nome@bodylab.com): ")
        plano = self.escolher_plano()
        turno = self.escolher_turno()
        self.__controlador_aluno.realizar_matricula(nome_aluno, numero_telefone, email , plano, turno)
        return self.assuntos_relacionados_a_matricula()

    def escolher_turno(self):
        turnos = {1: "Manhã", 2: "Tarde", 3: "Noite"}
        print("Escolha o turno:")

        for numero_turno, turno in turnos.items():
            print(f"{numero_turno} - {turno}")

        turno = int(input("Escolha o turno: "))
        if turno not in turnos:
            print("Operação inválida. Por favor, esoclha um número de 1 a 3.")
            return self.escolher_turno()
        else:
            return turnos[turno]

    def escolher_plano(self):
        planos = {1: "Gold", 2: "Silver", 3: "Diamond"}
        print("Escolha o plano: ")

        for numero_plano, plano in planos.items():
            print(f"{numero_plano} - {plano}")

        plano = int(input("Escolha o plano: "))
        if plano not in planos:
            print("Operação inválida. Por favor, esoclha um número de 1 a 3.")
            return self.escolher_plano()
        else:
            return planos[plano]
    
    def cancelar_matricula(self):
        id_matricula = input("Digite o código da matrícula (id_matricula): ")
        self.__controlador_aluno.cancelar_matricula(int(id_matricula))
        return self.assuntos_relacionados_a_matricula()

    def mostrar_dados_matricula(self):
        id_matricula = int(input("Digite o código da matrícula (id_matricula): "))
        self.__controlador_aluno.mostrar_dados_matricula(id_matricula)
        return self.assuntos_relacionados_a_matricula()

    def mostrar_dados_ficha(self):
        id_ficha = int(input("Digite o código da ficha (id_ficha): "))
        self.__controlador_aluno.mostrar_dados_ficha(id_ficha)

    def listar_alunos(self):
        print("Lista de alunos da BodyLab:")
        for aluno in self.__controlador_aluno.alunos:
            print(f"\nNome do aluno: {aluno.nome}\nID matricula: {aluno.matricula.id_matricula}\nTelefone: {aluno.numero_telefone}\nEmail: {aluno.email}\nTurno: {aluno.turno}\nPlano: {aluno.matricula.plano}\nMensalidade: {aluno.matricula.mensalidade}\n")
        self.mostrar_menu_inicial()

    def alterar_dado_matricula(self):
        print("Escolha o dado que deseja alterar:")
        print("1 - Plano")
        print("2 - Turno")
        opcao = int(input("Escolha a opção: "))

        if opcao == 1:
            self.alterar_plano()
        elif opcao == 2:
            self.alterar_turno()
        else:
            print("Opção inválida. Tente novamente.")
            self.alterar_dado_matricula()
        return self.assuntos_relacionados_a_matricula()
    
    def alterar_plano(self):
        id_matricula = int(input("Digite o código da matrícula (id_matricula): "))
        novo_plano = self.escolher_plano()
        self.__controlador_aluno.alterar_plano(id_matricula, novo_plano)
        return self.assuntos_relacionados_a_matricula()

    def alterar_turno(self):
        id_matricula = int(input("Digite o código da matrícula (id_matricula): "))
        novo_turno = self.escolher_turno()
        self.__controlador_aluno.alterar_turno(id_matricula, novo_turno)
        return self.assuntos_relacionados_a_matricula()

    def gerar_relatorios(self):
        print("---------------- Relatórios ----------------")
        print("1 - Calcular alunos por turno")
        print("2 - Calcular plano mais vendido")
        print("0 - retornar")

        opcao = int(input("Escolha a opção: "))

        if opcao == 1:
            self.__controlador_aluno.calcula_aluno_por_turno()
        elif opcao == 2:
            self.__controlador_aluno.calcula_plano_mais_vendido()
        elif opcao == 0:
            self.mostrar_menu_inicial()
        else:
            print("Opção inválida. Tente novamente.")
            self.gerar_relatorios()
