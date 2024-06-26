from simple_chalk import chalk, bold, yellowBright, red , green
from models.aluno import Aluno
from controllers.controladorAluno import ControladorAluno
from models.plano import Plano
from views.telaSistema import TelaSistema
from models.turno import Turno


class TelaAluno():
    def __init__(self):
        self.__controlador_aluno = ControladorAluno()
        self.__tela_sistema = TelaSistema()

    def mostrar_menu_inicial(self):
        while True:
            print()
            print(chalk.yellowBright.bold("----------- Aluno -------------"))
            print("Escolha a opção:")
            print("1 - Assuntos relacionados à matricula")
            print("2 - Assuntos relacionados à ficha")
            print("3 - Gerar relatórios")
            print("4 - Listar alunos")
            print("5 - Voltar para o menu inicial")
            print("0 - Sair")

            opcao = int(input(chalk.bold("Escolha a opção: ")))
            print(chalk.yellowBright.bold("-------------------------------"))

            if opcao == 1:
                self.assuntos_relacionados_a_matricula()
            elif opcao == 2:
                self.assuntos_relacionados_a_ficha()
            elif opcao == 3:
                self.gerar_relatorios()
            elif opcao == 4:
                self.listar_alunos()
            elif opcao == 5:
                break
            elif opcao == 0:
                exit(0)
            else:
                print(chalk.red("Opção inválida. Tente novamente. ❌"))

    def assuntos_relacionados_a_matricula(self):
        print()
        print(chalk.yellowBright.bold("------- Aluno -> Matrícula -------"))
        print("Escolha a opção:")
        print("1 - Realizar matrícula")
        print("2 - Cancelar matrícula")
        print("3 - Mostrar dados da matrícula")
        print("4 - Alterar algum dado da matrícula")
        print("0 - retornar")
        opcao = int(input(chalk.bold("Escolha a opção: ")))
        print(chalk.yellowBright.bold("----------------------------------"))
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
        print(chalk.yellowBright.bold("-------- Aluno -> Ficha ----------"))
        print("Escolha a opção:")
        print("1 - Mostrar treinos da ficha")
        print("0 - retornar")

        opcao = int(input(chalk.bold("Digite a opção: ")))

        if opcao == 1:
            self.mostrar_dados_ficha()
        elif opcao == 0:
            self.mostrar_menu_inicial()
        else:
            print("Opção inválida. Tente novamente.")
            self.assuntos_relacionados_a_ficha()

    def realizar_matricula(self):
        print()
        print(chalk.yellowBright.bold("------------ Aluno -> Ficha -------------"))
        while True:
            try:
                nome_aluno = input("Digite o nome do aluno: ")
                numero_telefone = int(input("Digite o número de telefone do aluno (ex:DD999999999): "))
                email = input("Digite o email do aluno (ex:nome@bodylab.com): ")
                plano = self.escolher_plano()
                turno = self.escolher_turno()
                self.__controlador_aluno.realizar_matricula(nome_aluno, numero_telefone, email , plano, turno)
                break
            except ValueError:
                print(chalk.red("Valor inserido é inválido, tente novamente: ❌"))
        return self.assuntos_relacionados_a_matricula()

    def escolher_plano(self):
        planos = {1: Plano.Gold, 2: Plano.Silver, 3: Plano.Diamond}
        print("Escolha o plano: ")

        for numero_plano, plano in planos.items():
            print(f"{numero_plano} - {plano.name}")

        plano = int(input("Escolha o plano: "))
        if plano not in planos:
            print(chalk.red("Operação inválida. Por favor, esoclha um número de 1 a 3. ❌"))
            return self.escolher_plano()
        else:
            return planos[plano]

    def escolher_turno(self):
        turnos = {1: Turno.matutino, 2: Turno.vespertino, 3: Turno.noturno}
        print("Escolha o turno:")

        for numero_turno, turno in turnos.items():
            print(f"{numero_turno} - {turno.name}")

        turno = int(input("Escolha o turno: "))
        if turno not in turnos:
            print(chalk.red("Operação inválida. Por favor, esoclha um número de 1 a 3. ❌"))
            return self.escolher_turno()
        else:
            return turnos[turno]
    
    def cancelar_matricula(self):
        id_matricula = input("Digite o código da matrícula (id_matricula): ")
        matricula_cancelada = self.__controlador_aluno.cancelar_matricula(int(id_matricula))
        if matricula_cancelada:
            print(chalk.green("Matrícula cancelada com sucesso. ✅"))
        else:
            print("Matrícula não encontrada.")
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
        id_matricula = int(input("Digite o código da matrícula (id_matricula): "))
        print("Escolha o dado que deseja alterar:")
        print("1 - Plano")
        print("2 - Turno")
        print("0 - Cancelar Operação")
        opcao = int(input(chalk.bold("Escolha a opção: ")))

        if opcao == 1:
            plano_novo = self.escolher_plano()
            self.__controlador_aluno.alterar_plano(id_matricula, plano_novo)
        elif opcao == 2:
            turno_novo = self.escolher_turno()
            self.__controlador_aluno.alterar_turno(id_matricula, turno_novo)
        elif opcao == 0:
            self.mostrar_menu_inicial()
        else:
            print(chalk.red("Opção inválida. Tente novamente. ❌"))
            self.alterar_dado_matricula()
        return self.assuntos_relacionados_a_matricula()
    

    def gerar_relatorios(self):
        print("---------------- Relatórios ----------------")
        print("1 - Calcular alunos por turno")
        print("2 - Calcular plano mais vendido")
        print("0 - retornar")

        opcao = int(input(chalk.bold("Escolha a opção: ")))

        if opcao == 1:
            print(self.__controlador_aluno.calcula_aluno_por_turno())
        elif opcao == 2:
            print(self.__controlador_aluno.calcula_plano_mais_vendido())
        elif opcao == 0:
            self.mostrar_menu_inicial()
        else:
            print(chalk.red("Opção inválida. Tente novamente. ❌"))
            self.gerar_relatorios()
