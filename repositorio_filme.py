from filme import Filme


class RepositorioFilme:
    def __init__(self):
        self.filme = []

    def cadastrar(self, filme: Filme):
        if self.buscar(filme.getCodigo()) is None:
            self.filme.append(filme)

        else:
            return print('Filme já cadastrado!')

    def buscar(self, codigo):
        for filme in self.filme:
            if filme.getCodigo() == codigo:
                return filme

            else:
                return None

    def atualizar(self, filme: Filme):
        filme = self.buscar(filme.getCodigo)
        if filme is not None:
            filme.setTitulo(filme.getTitulo)
            filme.setGeneros(filme.getGeneros)
            filme.setDataLancamento(filme.getDataLancamento)
            filme.setDiretor(filme.getDiretor)
            filme.setAtores(filme.getAtores)
            filme.setSinopse(filme.getSinopse)
            filme.setProdutores(filme.getProdutores)
            filme.setPrecoLocacao(filme.getPrecoLocacao)
            filme.setNumeroCopias(filme.getNumeroCopias)

        else:
            print('Filme não encontrado!')

    def deletar(self, codigo):
        for filme in self.filme:
            if filme.getCodigo() == codigo:
                self.filme.pop(self.filme.index(filme))
                print('Filme Deletado')

            else:
                print('Filme não encontrado!')

    def listar(self):
        return self.filme
