from conexDB import engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


conn = engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
Base = declarative_base()


class Produto (Base):

    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True )
    produto = Column(String(100), unique=True, index=True )
    desc_produto = Column(String(200), unique=True, index=True )
    qtd_produto = Column(Integer)
    valor = Column(String(100))

    def __repr__(self):
        return "Produto %s('%s', '%s', '%s','%s','%s')" % (self.id, self.produto, self.desc_produto, self.qtd_produto, self.valor)

    Base.metadata.create_all(engine)

