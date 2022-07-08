from operacao import Operacao


class Reserva (Operacao):
    def __init__(self, prioridade: int):
        super().__init__(self._cpf, self._codigo)
        self.prioridade = prioridade

    def setPrioridade(self, prioridade):
        self.prioridade = prioridade

    def getPrioridade(self):
        return self.prioridade
