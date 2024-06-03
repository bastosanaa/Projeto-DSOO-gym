from simple_chalk import chalk, magenta, red, bold

class TelaSistema():

    def le_num_inteiro(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError 
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def tela_opcoes(self):
            print()
            print(chalk.magenta.bold("---- Sistema BodyLab 🎯💪 ----"))
            print(chalk.bold("Escolha sua opção:"))
            print("1 - Professores")
            print("2 - Alunos")
            print("3 - Fichas")
            opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3])
            return opcao
        
        
