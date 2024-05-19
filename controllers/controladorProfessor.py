from models.professor import Professor
from models.turno import Turno

class ControladorProfessor():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__professores = []

    @property
    def professores(self):
        return self.__professores

    def acessar_professor_pelo_nome(self, nome) -> Professor:
        for prof in self.professores:
            if prof.nome == nome:
                return prof
        return None


    def cadastrar_professor(self, nome, telefone, email, turno, salario):
        if self.acessar_professor_pelo_nome(nome):
            return None
        novo_professor = Professor(nome, telefone, email, turno, salario)
        
        self.__professores.append(novo_professor)

    def remover_professor(self, nome, email):
        for professor in self.__professores:
            if professor.nome == nome and professor.email == email:
                self.__professores.remove(professor)
                return professor
        return None

    def escolher_turno(self, turno):
        lista_opcoes = {1: Turno.matutino, 2: Turno.vespertino, 3: Turno.noturno}
        return lista_opcoes[int(turno)]

    def alterar_turno(self,professor, turno):
        professor.turno = turno
        
    def calcular_professores_por_turno(self):
        turno_matutino = 0 
        turno_vespertino = 0
        turno_noturno = 0
        lista_turnos = {Turno.matutino: turno_matutino, Turno.vespertino: turno_vespertino, Turno.noturno: turno_noturno}
        for professor in self.professores:
            turno_encontrado = lista_turnos[professor.turno]
            turno_encontrado += 1
        return turno_matutino, turno_vespertino, turno_noturno

