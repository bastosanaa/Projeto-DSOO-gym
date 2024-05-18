from models.aluno import Aluno
from controllers.controladorAluno import ControladorAluno
from models.plano import Plano


class TelaAluno():
    def __init__(self):
        self.__controlador_aluno = ControladorAluno()

    def mostrar_menu_inicial(self):
        print("-------- Aluno ----------")
        print("Escolha a opção:")
        print("1 - Assuntos relacionados à matricula")
        print("2 - Assuntos relacionados à ficha")
        print("0 - retornar")

        opcao = int(input("Escolha a opção: "))

        if opcao == 1:
            self.assuntos_relacionados_a_matricula()
        elif opcao == 2:
            self.assuntos_relacionados_a_ficha()
        elif opcao == 0:
            exit(0)
        else:
            print("Opção inválida. Tente novamente.")
            self.mostrar_menu_inicial()

    def assuntos_relacionados_a_matricula(self):
        print("-------- Matrícula ----------")
        print("Escolha a opção:")
        print("1 - Realizar matrícula")
        print("2 - Cancelar matrícula")
        print("3 - Mostrar dados da matrícula")
        print("0 - retornar")
        opcao = int(input("Escolha a opção: "))
        if opcao == 1:
            self.realizar_matricula()
        elif opcao == 2:
            self.cancelar_matricula()
        elif opcao == 3:
            self.mostrar_dados_matricula()
        elif opcao == 0:
            self.mostrar_menu_inicial()
        else:
            print("Opção inválida. Tente novamente.")
            self.assuntos_relacionados_a_matricula()

    def assuntos_relacionados_a_ficha(self):
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
        nome_aluno = input("Digite o nome do aluno: ")
        numero_telefone = int(input("Digite o número de telefone do aluno (sem espaço): "))
        email = input("Digite o email do aluno: ")
        plano = self.escolher_plano()
        turno = self.escolher_turno()
        aluno = Aluno(nome_aluno, numero_telefone, email, turno, None)
        self.__controlador_aluno.realizar_matricula(aluno, plano, turno)
        return self.assuntos_relacionados_a_matricula()

    def escolher_turno(self):
        print("Escolha o turno:")
        print("1 - Manhã")
        print("2 - Tarde")
        print("3 - Noite")
        turno = int(input("Escolha o turno: "))
        if turno in [1, 2, 3]:
            return turno
        else:
            return "Operação inválida. Por favor, esoclha um número de 1 a 3."

    def escolher_plano(self):
        print("Escolha o plano:")
        print("1 - Gold")
        print("2 - Silver")
        print("3 - Diamond")
        plano = int(input("Escolha o plano: "))

        if plano in [1, 2, 3]:
            return Plano(plano)
        else:
            return "Operação inválida. Por favor, esoclha um número de 1 a 3."
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

