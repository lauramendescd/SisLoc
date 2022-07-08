from operacao import Operacao


class Locacao(Operacao):
    def __init__(self, Periodo: int):
        self.Periodo = Periodo

    def setPeriodo(self, Periodo):
        self.Periodo = Periodo

    def getPeriodo(self, Periodo):
        return self.Periodo
