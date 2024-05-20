from simple_chalk import chalk, magenta, bold

class TelaSistema():
    def tela_opcoes(self):
        while True:
            print(chalk.magenta.bold("---- Sistema BodyLab ----"))
            print("Escolha sua opção:")
            print("1 - Professores")
            print("2 - Alunos")
            print("3 - Fichas")
            opcao = int(input("Escolha a opcao: "))
    
            if opcao not in [1,2,3]:
                print()
                print("Opção inválida. Tente novamente.")
                print()
                continue
            return opcao
        
