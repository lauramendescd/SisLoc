class Cliente:
    def __init__(self, cpf: str):
        self._cpf = cpf
        self._nome = str()
        self._endereco = str()

    def setCpf(self,Cpf: str):
        self.cpf = Cpf

    def getCpf(self):
        return self.cpf

    def setNome(self, Nome:str):
        self.nome = Nome

    def getNome(self):
        return self.nome

    def setEndereco(self, Endereco:str):
        self.endereco = Endereco

    def getEndereco(self):
        return self.endereco

    def imprimir(self):
        print('Nome{},  Endereço{}').format(self.nome,self.endereco)
