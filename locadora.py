from repositorio_filme import RepositorioFilme
from repositorio_cliente import RepositorioCliente
from repositorio_operacao import RepositorioOperacao
class Locadora:
    def __init__(self, filmes:RepositorioFilme, clientes:RepositorioCliente, operacoes:RepositorioOperacao):
        self._filmes = RepositorioFilme
        self._clientes = RepositorioCliente
        self._operacoes = RepositorioOperacao

    def cadastrarCliente(self, cliente: Cliente):
        for  in self.locadora:
            if cliente.getCpf() == cl:
                return cliente

    def buscarCliente(self, cpf:str):
        for cliente in self._clientes:
            if cliente.getCpf() == cpf :
                return cliente

            else:
                return None

    def atualizarCadastroCliente(self, cliente:Cliente):

    def removerCliente(self, cpf:str):

    def cadastrarFilme(self, filme:Filme):

    def buscarFilme(self,codigo: int):

    def atualizarCadastroFilme(self, filme:Filme):

    def removerFilme(self,codigo:int):

    def reservarFilme(self, cpf:str, codigo:int):

    def finalizarReservaFilme(self, cpf:str, codigo:int):

    def locarFilme(self, cpf:str, codigo:int):

    def devolverFilme(self, cpf:str, codigo:int):

    def ImprimirHistoricoLocacoes(self, cpf:str):

    def ImprimirFilmes(self, top:int):