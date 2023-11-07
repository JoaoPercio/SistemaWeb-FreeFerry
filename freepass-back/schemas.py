from datetime import date
from typing import List  
from pydantic import BaseModel

class AdministradorBase(BaseModel):
    email: str   
class AdministradorCreate(AdministradorBase):
    senha: str
class Administrador(AdministradorBase):
    id: int
    class Config:
        orm_mode = True
class AdministradorLoginSchema(BaseModel):
    email: str
    senha: str
    class Config:
        schema_extra = {
            "example": {
                "email": "x@x.com",
                "senha": "pass"
            }
        }
class PaginatedAdministrador(BaseModel):
    limit: int
    offset: int
    data: List[Administrador]
class EnderecoBase(BaseModel):
    Cep: str
    Estado: str
    Cidade: str
    Bairro: str
    Logradouro: str
    Complemento: str
    Id_Usuario: int
    Numero: int
class EnderecoCreate(EnderecoBase):
    pass
class Endereco(EnderecoBase):
    Id: int
    class Config:
        orm_mode = True
class PaginatedEndereco(BaseModel):
    limit: int
    offset: int
    data: List[Endereco]


class UsuarioBase(BaseModel):
    Nome_Completo: str
    Telefone: str
    Email: str
    Senha: str
    Cpf: str
    Status: int
    Passe_Quantidade: int
    Passe_Categoria : bool
    Motociclista: bool
    Data_Cadastro: date
class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    Id: int
    endereco: Endereco = {}
    class Config:
        orm_mode = True
class PaginatedUsuario(BaseModel):
    limit: int
    offset: int
    data: List[Usuario]

class DocumentoBase(BaseModel):
    Nome : str
    Url : str
    IsPasse : bool
    Id_Usuario: int
class DocumentoCreate(DocumentoBase):
    pass
class Documento(DocumentoBase):
    Id: int
    class Config:
        orm_mode = True
class PaginatedDocumento(BaseModel):
    limit: int
    offset: int
    data: List[Documento]

