from models import Pedido

class PedidoRepository:

    def __init__(self, session):
        self.session = session

    def adicionar(self, pedido):
        self.session.add(pedido)
        self.session.commit()

    def listar(self):
        return self.session.query(Pedido).all()

    def buscar_por_id(self, id):
        return self.session.get(Pedido, id)

    def excluir(self, id):
        pedido = self.buscar_por_id(id)
        if pedido:
            self.session.delete(pedido)
            self.session.commit()
            return True
        return False