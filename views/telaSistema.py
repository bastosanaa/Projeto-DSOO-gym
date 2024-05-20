from simple_chalk import chalk, magenta, bold

class TelaSistema():
    def tela_opcoes(self):
        while True:
            print(chalk.magenta.bold("---- Sistema BodyLab ----"))
            print(chalk.bold("Escolha sua opção:"))
            print("1 - Professores")
            print("2 - Alunos")
            print("3 - Fichas")
            opcao = int(input("Digite a opcao: "))
    
            if opcao not in [1,2,3]:
                print()
                print(chalk.red("Opção inválida. Tente novamente. ❌"))
                print()
                continue
            return opcao
        
