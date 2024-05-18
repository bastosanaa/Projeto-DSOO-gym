from datetime import datetime, timedelta
import random
from models.matricula import Matricula
from models.plano import Plano
from controllers.controladorFicha import ControladorFicha
from models.aluno import Aluno

# from controllers.controladorMatricula import ControladorMatricula

class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__planos = [Plano.Diamond, Plano.Gold, Plano.Silver]
        self.__contraladorFicha = ControladorFicha(self)

    @property
    def planos(self):
        return self.__planos

    @property
    def alunos(self):
        return self.__alunos

    def get_aluno(self, nome_aluno):
            for aluno in self.__alunos:
                if aluno.nome == nome_aluno:
                    return aluno
            return None
    ################################ matricula ########################################

    def realizar_matricula(self, nome_aluno, numero_telefone, email, plano, turno):
        aluno = Aluno(nome_aluno, numero_telefone, email, turno, None)
        aluno_existente = self.get_aluno(aluno.nome)
        if aluno_existente:
            print("Aluno já matriculado.")
            return

        id_matricula = random.randint(1000, 9999)
        mensalidade = self.definir_mensalidade_de_acordo_com_plano(plano)
        data_inicio_matricula = datetime.now()
        data_vencimento_matricula = data_inicio_matricula + timedelta(days=30)
        data_termino_matricula = data_inicio_matricula + timedelta(days=365)

        matricula = Matricula(id_matricula, turno, plano, mensalidade, aluno, data_inicio_matricula,
                              data_vencimento_matricula, data_termino_matricula)
        aluno.matricula = matricula
        self.__alunos.append(aluno)
        print(f"Matrícula realizada com sucesso.\nID da matrícula: {matricula.id_matricula}")

    def definir_mensalidade_de_acordo_com_plano(self, plano: Plano):
        mensalidade = 0.0
        if plano == Plano.Diamond:
            mensalidade += 200.00
        elif plano == Plano.Gold:
            mensalidade += 150.00
        else:
            mensalidade += 100.00
        return mensalidade

    def cancelar_matricula(self, id_matricula):
        for aluno in self.__alunos:
            if aluno.matricula.id_matricula == id_matricula:
                self.__alunos.remove(aluno)
                print("Matrícula cancelada com sucesso.")
            else:
                print("Matrícula não encontrada.")

    def buscar_matricula_por_id(self, id_matricula):
        for aluno in self.__alunos:
            if aluno.matricula.id_matricula == id_matricula:
                return aluno.matricula
        return None

    def mostrar_dados_matricula(self, id_matricula):
        matricula = self.buscar_matricula_por_id(id_matricula)
        if matricula:
            print("-------- Dados da Matrícula ----------")
            print("Nome: ", matricula.aluno.nome)
            print("Plano: ", matricula.plano)
            print("Turno: ", matricula.turno)
            print("Data de Início: ", matricula.data_inicio_matricula)
            print("Data de Término: ", matricula.data_termino_matricula)
            print("Data de Vencimento da Mensalidade: ", matricula.data_vencimento_matricula)
            print("Mensalidade: ", matricula.mensalidade)
        else:
            print("Matrícula não encontrada.")

    def alterar_plano(self, id_matricula, novo_plano):
        matricula = self.buscar_matricula_por_id(id_matricula)
        if matricula:
            matricula.plano = novo_plano
            print("Plano alterado com sucesso.")
        else:
            print("Matrícula não encontrada.")

    def alterar_turno(self, id_matricula, novo_turno):
        matricula = self.buscar_matricula_por_id(id_matricula)
        if matricula:
            matricula.turno = novo_turno
            print("Turno alterado com sucesso.")
        else:
            print("Matrícula não encontrada.")

########################### ficha ##############################################
    
    def buscar_ficha(self, id_ficha):
        for ficha in self.__contraladorFicha.fichas:
            if ficha.id_ficha == id_ficha:
                return ficha
        return None
    
    def mostrar_dados_ficha(self, ficha):
        print("-------- Dados da Ficha ----------")
        print("ID da Ficha: ", ficha.id_ficha)
        print("Descrição: ", ficha.descricao)
        print("Professor Responsável: ", ficha.prof_responsavel.nome)
        print("Treinos: ", ficha.treinos)
        
############################ relátorios ####################################################
    def calcular_aluno_por_turno(self):
        alunos_por_turno = {}
        for aluno in self.__alunos:
            turno = aluno.turno
            if turno in alunos_por_turno:
                alunos_por_turno[turno] += 1
            else:
                alunos_por_turno[turno] = 1
        for turno, quantidade in alunos_por_turno.items():
            print(f"Turno: {turno} - Quantidade de alunos: {quantidade}")

    def calcula_plano_mais_vendido(self):
        plano_mais_vendido = ''
        quantidade_vendas = 0
        for plano in self.__planos:
            vendas_plano = 0
            for aluno in self.__alunos:
                if aluno.matricula.plano == plano:
                    vendas_plano += 1
                if vendas_plano > quantidade_vendas:
                    quantidade_vendas = vendas_plano
                    plano_mais_vendido = plano
        return plano_mais_vendido
