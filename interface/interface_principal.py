class InterfacePrincipal:

    def __init__(self, usuario_service, produto_service, pedido_service):
        self.usuario_service = usuario_service
        self.produto_service = produto_service
        self.pedido_service = pedido_service