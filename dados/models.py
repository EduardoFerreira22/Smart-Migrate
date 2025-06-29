from sqlalchemy import Column, Integer, String, Text, DateTime, Date, Float, Boolean, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Contabilidade(Base):
    __tablename__ = 'contabilidade'
    id = Column(Integer, primary_key=True)
    status = Column(Boolean, default=True)
    cpf_cnpj = Column(String(15))
    nome = Column(String(150), nullable=False)
    razao_social = Column(String(150))
    email = Column(String(100))
    telefone = Column(String(10))

    clientes = relationship("Cliente", back_populates="contabilidade")

    def __repr__(self):
        return f"<Contabilidade(nome={self.nome}, contato={self.contato})>"

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    status = Column(Boolean, default=True)
    status_envio = Column(String(50), default='Não Enviado')
    cnpj = Column(String(15))
    nome = Column(String(150), nullable=False)
    razao_social = Column(String(150))
    email = Column(String(100))
    contabilidade_id = Column(Integer, ForeignKey('contabilidade.id'), nullable=True)
    sistema_erp = Column(String(50))
    link_sistema = Column(String(300))
    user_sistema = Column(String(50))
    senha_sistema = Column(String(50))
    cert_path = Column(String(300))
    senha_cert= Column(String(100))

    contabilidade = relationship("Contabilidade", back_populates="clientes")

    def __repr__(self):
        return f"<Cliente(nome={self.nome}, contabilidade_id={self.contabilidade_id})>"
    

class MDE_XML(Base):
    id = Column(Integer, primary_key=True)
    numero_nf = Column(Integer)
    valor_nf = Column(Float(10,2))
    destinatario = Column(String(150))
    cnpj_destinatario = Column(String(15))
    data_emissao = Column(Date)
    chave_nf = Column(String(50))
    ultimo_nfu = Column(Integer)
    xml_completo = Column(Boolean)
    conteudo_xml = Column(Text)
    justificativa_op_Nrealizada = Column(String)
    ciencia_operacao = Column(Boolean)
    confirmar_operacao = Column(Boolean)
    desconhecer_operacao = Column(Boolean)
    operacao_nao_realizada = Column(Boolean)
    download_xml = Column(Boolean)
    data_registro = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<MDE_XML(destinatario={self.destinatario}, cnpj_destinatario={self.cnpj_destinatario})>"





