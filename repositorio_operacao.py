from operacao import Operacao
from reserva import Reserva
from locacao import Locacao


class RepositorioOperacao:
    def __init__(self):
        self.operacao = []

    def cadastrar(self, operacao: Operacao):
        if operacao in self.operacao:
            print('Operação já cadastrada!')
        else:
            operacao.setAtivo(True)
            self.operacao.append(operacao)

    def buscarReservas(self, cpf: str):
        reservas = []
        for operacao in self.operacao:
            if isinstance(operacao, Reserva):
                if operacao.getCpf() == cpf:
                    if operacao.getAtivo() is True:
                        reservas.append(operacao)
                        return reservas

            else:
                print('A reserva não existe')

    def buscarLocacoes(self, cpf: str):
        locacoes = []
        for operacao in self.operacao:
            if isinstance(operacao, Locacao):
                if operacao.getCpf() == cpf:
                    if operacao.getAtivo() is True:
                        locacoes.append(operacao)
                        return locacoes
            else:
                print('A locação não existe')


    def deletarReserva(self, cpf: str, codigo: int):
        for reserva in self.operacao:
            if reserva.getCpf() == cpf and reserva.getCodigo() == codigo and isinstance(reserva, Reserva):
                reserva.setAtivo(False)

    def deletarLocacao(self, cpf: str, codigo: int):
        for locacao in self.operacao:
            if locacao.getCpf() == cpf and locacao.getCodigo() == codigo and isinstance(locacao, Locacao):
                locacao.setAtivo(False)

    def listarLocacoes(self, cpf: str):
        locacoesLista = []
        for operacao in self.operacao:
            if operacao.getCpf() == cpf:
                if isinstance(locacoesLista, Locacao):
                    self.operacao.append(locacoesLista)
                    return locacoesLista
            else:
                print('Locação nao encontrada para o cpf')

    def numeroLocacoesCpf(self, cpf: str):
        count = 0
        for locacao in self.operacao:
            if locacao.getCpf() == cpf:
                if isinstance(locacao, Locacao):
                    if locacao.getAtivo() is True:
                        count += 1
        return count

    def numeroLocacoesCodigo(self, codigo: int):
        count = 0
        for locacao in self.operacao:
            if locacao.getCodigo() == codigo:
                if isinstance(locacao, Locacao):
                    if locacao.getAtivo() is True:
                        count += 1
        return count


    def numeroLocacoesAtivasCpf(self, cpf: str):
    count = 0
    for operacao in self.operacao:
        if operacao.getCpf() == cpf:
            if isinstance(operacao, Locacao):
                if operacao.getAtivo() is True:
                    count += 1
    return count


def numeroLocacoesAtivasCodigo(self, codigo: int):
    count = 0
    for operacao in self.operacao:
        if operacao.getCodigo() == codigo:
            if isinstance(operacao, Locacao):
                if operacao.getAtivo() is True:
                    count += 1
    return count


def numeroReservas(self, codigo: int):
    count = 0
    for operacao in self.operacao:
        if operacao.getCodigo() == codigo:
            if isinstance(operacao, Reserva):
                if operacao.getAtivo() is True:
                    count += 1
    return count
