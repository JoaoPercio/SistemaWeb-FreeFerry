from sqlalchemy import Column, Integer, String, SmallInteger, Date, ForeignKey, Table, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base

class Administrador(Base):
    __tablename__ = "administrador"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(300))
    senha = Column(String(150))

class Usuario(Base):
    __tablename__ = "Usuario"

    Id = Column(Integer, primary_key=True, index=True)
    Nome_Completo = Column(String(80))
    Telefone = Column(String(15))
    Email = Column(String(80))
    Senha = Column(String(256))
    Cpf = Column(String(15))
    Status = Column(Integer)
    Passe_Quantidade = Column(Integer)
    Passe_Categoria = Column(Boolean)
    Motociclista = Column(Boolean)
    Data_Cadastro = Column(Date)
    Documentos = relationship("Documento", uselist=False, back_populates="Usuario", cascade="all, delete-orphan")
    endereco = relationship("Endereco", uselist=False, back_populates="usuario")


class Endereco(Base):
    __tablename__ = "Endereco"

    Id = Column(Integer, primary_key=True, index=True)
    Cep = Column(String(10))
    Estado = Column(String(50))
    Cidade = Column(String(50))
    Bairro = Column(String(50))
    Logradouro = Column(String(50))
    Complemento = Column(String(50))
    Id_Usuario = Column(Integer, ForeignKey("Usuario.Id"), nullable=False)
    Numero = Column(Integer)

    usuario = relationship("Usuario", uselist=False, back_populates="endereco")

class Documento(Base):
    __tablename__ = "Documento"

    Id = Column(Integer, primary_key=True, index=True)
    Nome = Column(String(80))
    Url = Column(String(256))
    IsPasse = Column(Boolean)
    Id_Usuario = Column(Integer, ForeignKey("Usuario.Id"), nullable=False)
    Usuario = relationship("Usuario", uselist=False, back_populates="Documentos")


    
