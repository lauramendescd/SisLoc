from cliente import Cliente


class RepositorioCliente:
    def __init__(self):
        self.clientes = []

    def cadastrar(self, cliente: Cliente):
        if self.buscar(cliente.getCpf()) is None:
            self.clientes.append(cliente)

        else:
            return print('Cliente já cadastrado!')

    def buscar(self, cpf: str):
        for cliente in self.clientes:
            if cliente.getCpf() == cpf:
                return cliente

            else:
                return None

    def atualizar(self, cliente: Cliente):
        cliente = self.buscar(cliente.getCpf())
        if cliente is not None:
            cliente.setNome(cliente.getNome)
            cliente.setEndereco(cliente.getEndereco)

        else:
            print('Cliente não encontrado!')

    def deletar(self):
        for clientes in self.clientes:
            if clientes.getCpf() == 'cpf':
                self.clientes.pop(self.clientes.index(clientes))
                print('Cliente Deletado')

            else:
                print('Cliente não encontrado!')

    def listar(self):
        return self.clientes
