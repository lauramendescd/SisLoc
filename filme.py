from datetime import date


class Filme:
    def __init__(self, codigo:int, titulo:str):
        self._codigo = codigo
        self._titulo = titulo
        self._generos = list()
        self._dataLancamento = date.today()
        self._diretor = str()
        self._atores = list()
        self._sinopse = str()
        self._produtores = list()
        self._precoLocacao = float()
        self._numeroCopias = int()

    def setCodigo(self,Codigo:int):
        self._codigo = Codigo

    def getCodigo(self):
        return self._codigo

    def setTitulo(self,Titulo:str):
        self._titulo = Titulo

    def getTitulo(self):
        return self._titulo

    def setGeneros(self,Genero:list):
        self._generos = Genero

    def getGeneros(self):
        return self._generos

    def addGeneros(self,Genero:str):
        self._generos.append(Genero)

    def setDataLancamento(self,DataLancamento: date):
        self._dataLancamento = DataLancamento

    def getDataLancamento(self):
        return self._dataLancamento

    def setDiretor(self,Diretor:str):
        self._diretor = Diretor

    def getDiretor(self):
        return self._diretor

    def setAtores(self,Atores:list):
        self._atores = Atores

    def getAtores(self):
        return self._atores

    def addAtor(self,Ator:str):
        self._atores.append(Ator)

    def setSinopse(self,Sinopse:str):
        self._sinopse = Sinopse

    def getSinopse(self):
        return self._sinopse

    def setProdutores(self, Produtores:list):
        self._produtores = Produtores

    def getProdutores(self):
        return self._produtores

    def AddProdutor(self, Produtores:str):
        self._produtores.append(Produtores)

    def setPrecoLocacao(self,PrecoLocacao:float):
        self._precoLocacao = PrecoLocacao

    def getPrecoLocacao(self):
        return self._precoLocacao

    def setNumeroCopias(self,NumeroCopias:int):
        self._numeroCopias = NumeroCopias

    def getNumeroCopias (self):
        return self._numeroCopias

    def imprimir(self):
        print('Codigo {}, Titulo{}, Generos{}, Lancamento{}, Diretor{}, Atores{}, Sinopse{} ').format(self._codigo, self._titulo, self._generos, self._dataLancamento, self._diretor, self._atores, self._sinopse)