from simple_chalk import chalk, magenta, red, bold

class TelaSistema():
    def tela_opcoes(self):
        while True:
            print()
            print(chalk.magenta.bold("---- Sistema BodyLab 🎯💪 ----"))
            print(chalk.bold("Escolha sua opção:"))
            print("1 - Professores")
            print("2 - Alunos")
            print("3 - Fichas")
            try:
                opcao = int(input("Digite a opcao: "))
            except ValueError:
                print()
                print(chalk.red("Opção inválida. Tente novamente. ❌"))
                continue
            print(chalk.magenta.bold("-------------------------------"))
    
            if opcao not in [1,2,3]:
                print()
                print(chalk.red("Opção inválida. Tente novamente. ❌"))
                continue
            return opcao
        
        
