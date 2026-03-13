from models import Produto

class ProdutoRepository:

    def __init__(self, session):
        self.session = session

    def adicionar(self, produto):
        self.session.add(produto)
        self.session.commit()

    def listar(self):
        return self.session.query(Produto).all()

    def buscar_por_id(self, id):
        return self.session.get(Produto, id)

    def excluir(self, id):
        produto = self.buscar_por_id(id)
        if produto:
            self.session.delete(produto)
            self.session.commit()
            return True
        return False