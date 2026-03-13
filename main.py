# python -m venv .venv
# .venv\Scripts\activate
# pip freeze > requirements.txt
# pip install -r requirements.txt
# python main.py

from database import Session
from repositories.usuario_repository import UsuarioRepository
from services.usuario_service import UsuarioService
from interface.interface_principal import InterfacePrincipal

session = Session()

usuario_repo = UsuarioRepository(session)
usuario_service = UsuarioService(usuario_repo)

app = InterfacePrincipal(usuario_service)
app.run()