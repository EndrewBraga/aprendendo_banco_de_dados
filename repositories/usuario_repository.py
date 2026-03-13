from models import Usuario

class UsuarioRepository:

    def __init__(self, session):
        self.session = session

    def adicionar(self, usuario):
        self.session.add(usuario)
        self.session.commit()

    def listar(self):
        return self.session.query(Usuario).all()

    def buscar_por_id(self, id):
        return self.session.get(Usuario, id)

    def excluir(self, id):
        usuario = self.buscar_por_id(id)
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
            return True
        return False