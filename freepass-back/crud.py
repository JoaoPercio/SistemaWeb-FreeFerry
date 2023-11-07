from sqlalchemy.orm import Session
from exceptions import UsuarioNotFoundError,UsuarioAlreadyExistError
import bcrypt, models, schemas

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do servidor SMTP do Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'jp.percito@gmail.com'
sender_password = 'slkbtiuhroxfsowy'

#usuario

def check_administrador(db: Session, administrador: schemas.AdministradorLoginSchema):
    db_administrador = db.query(models.Administrador).filter(models.Administrador.email == administrador.email).first()
    if db_administrador is None:
        return False
    if administrador.senha == db_administrador.senha:
        return True
    else:
        return False

def get_administrador_by_email(db: Session, administrador_email: str):
    return db.query(models.Administrador).filter(models.Administrador.email == administrador_email).first()

def create_administrador(db: Session, administrador: schemas.AdministradorCreate):
    db_administrador = get_administrador_by_email(db, administrador.email)
    # O parâmetro rounds do gensalt determina a complexidade. O padrão é 12.
    if db_administrador is not None:
        raise UsuarioAlreadyExistError
    db_administrador = models.Administrador(**administrador.dict())
    db.add(db_administrador)
    db.commit()
    db.refresh(db_administrador)
    return db_administrador


def get_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = db.query(models.Usuario).get(usuario_id)
    if db_usuario is None:
        raise UsuarioNotFoundError
    return db_usuario

def get_all_usuarios(db: Session, offset: int, limit: int):
    return db.query(models.Usuario).filter(models.Usuario.Status == 1).offset(offset).limit(limit).all()

def get_all_usuarios_passe(db: Session, offset: int, limit: int):
    return db.query(models.Usuario).filter(models.Usuario.Status == 3).offset(offset).limit(limit).all()

def delete_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = get_usuario_by_id(db, usuario_id)
    if db_usuario.Status == 1:
        db.query(models.Documento).filter(models.Documento.Id_Usuario == usuario_id).delete()
        db.delete 
        db.delete(db_usuario)
        db.commit()
        # Crie uma mensagem MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = db_usuario.Email
        msg['Subject'] = 'Cadastro Negado'
        
        # Corpo do email
        body = "Seu cadastro foi negado no programa passe livre, revise suas informações e documentos com cuidado e refaça seu cadastro."
        msg.attach(MIMEText(body, 'plain'))

        # Inicie uma conexão com o servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Inicie a criptografia TLS

        # Faça login na conta
        server.login(sender_email, sender_password)

        # Envie o email
        text = msg.as_string()
        server.sendmail(sender_email, db_usuario.Email, text)

        # Encerre a conexão
        server.quit()
        return
    else:
        db_usuario = get_usuario_by_id(db, usuario_id)
        db_usuario.Status = 2
        db.commit()
        db.refresh(db_usuario)
        # Crie uma mensagem MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = db_usuario.Email
        msg['Subject'] = 'Solicitação de passe negada'
        
        # Corpo do email
        body = "sua solicitação de passe mensal foi negada, acesse seu aplicativo para refaze-la."
        msg.attach(MIMEText(body, 'plain'))

        # Inicie uma conexão com o servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Inicie a criptografia TLS

        # Faça login na conta
        server.login(sender_email, sender_password)

        # Envie o email
        text = msg.as_string()
        server.sendmail(sender_email, db_usuario.Email, text)

        # Encerre a conexão
        server.quit()
        return

def update_usuario(db: Session, usuario_id: int):
    db_usuario = get_usuario_by_id(db, usuario_id)
    if db_usuario.Status== 1:
        db_usuario.Status = 2
        db.commit()
        db.refresh(db_usuario)
         # Crie uma mensagem MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = db_usuario.Email
        msg['Subject'] = 'Cadastro Aprovado'
        
        # Corpo do email
        body = "Seu cadastro foi Aprovado no programa passe livre, seu acesso ao aplicativo já está disponivel."
        msg.attach(MIMEText(body, 'plain'))

        # Inicie uma conexão com o servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Inicie a criptografia TLS

        # Faça login na conta
        server.login(sender_email, sender_password)

        # Envie o email
        text = msg.as_string()
        server.sendmail(sender_email, db_usuario.Email, text)

        # Encerre a conexão
        server.quit()
        return db_usuario
    else:
        db_usuario.Status = 4
        db_usuario.Passe_Quantidade = 40
        db.commit()
        db.refresh(db_usuario)
         # Crie uma mensagem MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = db_usuario.Email
        msg['Subject'] = 'Solicitação de passe Aprovada'
        
        # Corpo do email
        body = "Sua solicitação de passes mensais foi aprovada, acesse o aplicativo para utilizar seus passes."
        msg.attach(MIMEText(body, 'plain'))

        # Inicie uma conexão com o servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Inicie a criptografia TLS

        # Faça login na conta
        server.login(sender_email, sender_password)

        # Envie o email
        text = msg.as_string()
        server.sendmail(sender_email, db_usuario.Email, text)

        # Encerre a conexão
        server.quit()
        return db_usuario


def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_all_documentos(db: Session,usuario_id:int, offset: int, limit: int):
    db_usuario =get_usuario_by_id(db, usuario_id) 
    if(db_usuario.Status==1):
        print("passo aqui")
        return db.query(models.Documento).filter(models.Documento.Id_Usuario == usuario_id).filter(models.Documento.IsPasse == False).offset(offset).limit(limit).all()
    else:
        print("passo aqui 2")
        return db.query(models.Documento).filter(models.Documento.Id_Usuario == usuario_id).filter(models.Documento.IsPasse == True).offset(offset).limit(limit).all()

def create_documento(db: Session, usuario: schemas.DocumentoCreate):
    db_documento = models.Documento(**usuario.dict())
    db.add(db_documento)
    db.commit()
    db.refresh(db_documento)
    return db_documento


def create_endereco(db: Session, registro: schemas.EnderecoCreate):
    db_endereco = models.Endereco(**registro.dict())
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco

