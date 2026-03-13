from models import Produto

class ProdutoService:

    def __init__(self, produto_repo):
        self.produto_repo = produto_repo

    def cadastrar_produto(self, nome, preco):

        if preco <= 0:
            raise ValueError("Preço inválido")

        produto = Produto(nome, preco)
        self.produto_repo.adicionar(produto)

    def listar_produtos(self):
        return self.produto_repo.listar()