from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    preco = Column(Integer)

    pedidos = relationship("Pedido", back_populates="produto")