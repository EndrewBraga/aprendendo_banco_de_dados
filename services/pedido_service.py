from models import Pedido

class PedidoService:

    def __init__(self, pedido_repo, usuario_repo, produto_repo):
        self.pedido_repo = pedido_repo
        self.usuario_repo = usuario_repo
        self.produto_repo = produto_repo

    def criar_pedido(self, usuario_id, produto_id, quantidade):

        usuario = self.usuario_repo.buscar_por_id(usuario_id)
        if not usuario:
            raise ValueError("Usuário não encontrado")

        produto = self.produto_repo.buscar_por_id(produto_id)
        if not produto:
            raise ValueError("Produto não encontrado")

        if quantidade <= 0:
            raise ValueError("Quantidade inválida")

        pedido = Pedido(usuario_id, produto_id, quantidade)
        self.pedido_repo.adicionar(pedido)

        total = produto.preco * quantidade
        return total

    def listar_pedidos(self):
        return self.pedido_repo.listar()