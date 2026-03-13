from models import Usuario

class UsuarioService:

    def __init__(self, usuario_repo):
        self.usuario_repo = usuario_repo

    def cadastrar_usuario(self, nome, email, senha):

        if len(senha) < 4:
            raise ValueError("Senha muito curta")

        usuario = Usuario(nome, email, senha)
        self.usuario_repo.adicionar(usuario)

    def listar_usuarios(self):
        return self.usuario_repo.listar()