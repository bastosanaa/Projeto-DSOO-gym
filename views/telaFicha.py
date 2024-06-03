from simple_chalk import chalk, blue, green, red, bold, yellow
from models.ficha import Ficha
from controllers.controladorFicha import ControladorFicha
from controllers.controladorProfessor import ControladorProfessor
from views.telaSistema import TelaSistema

class TelaFicha():
    def __init__(self):
        self.__controlador_ficha = ControladorFicha()
        self.__controlador_professor = ControladorProfessor()
        self.__tela_sistema = TelaSistema()

    def mostrar_menu_inicial(self):
        while True:
            if not self.__controlador_professor.professores:
                print()
                print(chalk.yellow("!!! Nenhum professor cadastrado !!!"))
                print(chalk.bold("Obs: deve haver ao menos um professor cadastrado para que as fichas sejam manipuladas"))
                print()
                break
            print()
            print(chalk.blue("-------- Fichas ----------"))
            print("1 - mostrar todas as fichas")
            print("2 - cadastrar ficha")
            print("3 - excluir ficha pelo id")
            print("0 - Voltar ao menu inicial")
            resposta_usuario = input("Insira a opção escolhida: ")
            print(chalk.blue("--------------------------"))
            
            if resposta_usuario == "1":
                self.mostrar_fichas()
            elif resposta_usuario == "2":
                self.criar_fichas()
            elif resposta_usuario == "3":
                id = input("Qual o id da ficha que você deseja excluir?")
                print("digite 0 para voltar ao menu inicial")
                if id == "0":
                    continue
                self.__controlador_ficha.excluir_ficha_pelo_id(id)
            elif resposta_usuario == "0":
                break
            else:
                print(chalk.red("Opção inválida. Tente novamente. ❌"))
                self.mostrar_menu_inicial()

    def mostrar_fichas(self):
        print()
        if self.__controlador_ficha.fichas:
            for ficha in self.__controlador_ficha.fichas:
                print()
                print(chalk.blue(f'---- {ficha.descricao} ---'))
                print (f'ID: {ficha.id_ficha}')
                print(f'Criada por: {ficha.prof_responsavel.nome}')
                print(chalk.blue("-" * len(ficha.descricao)))
        else:
            print('Nenhuma ficha cadastrada')
            self.mostrar_menu_inicial()
        


    def criar_fichas(self):
        print()
        descricao = input("Descreva o treino da ficha a criar: ")
        professor = None
        treinos = []
        while not professor:
            nome_professor = input("Escolha um professor pelo nome: ")
            professor = self.__controlador_ficha.controlador_professor.acessar_professor_pelo_nome(nome_professor)
            if not professor:
                print(chalk.red("Professor não encontrado, insira um professor válido. ❌"))
        n_treinos = int(input("Quantos treinos terá a ficha? "))
        for _ in range(n_treinos):
            treino = input("Insira o(s) grupo(s) muscular do treino: ")
            treinos.append(treino)
            input(chalk.green('Ficha criada com sucesso! ✅'))
        return descricao, professor, treinos
        self.mostrar_menu_inicial()
    
    def excluir_ficha_pelo_id(self):
        print()
        menu = input("deseja exibir as fichas? (s / n)")
        if menu == "s":
            self.mostrar_fichas()
        else:
            print()
            id = input("Qual o id da ficha que você deseja excluir?")
            ficha = self.__controlador_ficha.excluir_ficha_pelo_id(id)
            if ficha:
                print()
                print(chalk.green(f"Ficha de id:{id} excluida com sucesso! ✅"))
            else:
                print(chalk.red("Ficha não encontrada ❌"))
                self.mostrar_menu_inicial()
