from sqlalchemy import Column, String, Integer, DateTime, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  models import Base, Contato


class Passageiro(Base):

    # Comentário de aula: a tabela no banco pode seguir um menemônico e 
    # ter um nome diferente do que poderia ser "mais apropriado". Aqui 
    # a tabela que vai representar o produto, se chama 'prod_catalog',
    # supondo o cenário em que o sufixo "catalog" é utilizado para 
    # indicar que é uma tabela de catálogo de produtos.
    __tablename__ = 'passageiro'

    # O nome de uma coluna também pode ter no banco um nome diferente
    # como é apresentado aqui no caso do Produto.id que no banco será 
    # prod_catalog.pk_prod, o sufixo pk está sendo utilizado para 
    # indicar que é uma chave primária
    id = Column("pk_passageiro", Integer, primary_key=True)

    # Supondo que os atributos seguintes já estejam em conformidade
    # com o menemônico adotado pela empresa, então não há necessidade
    # de fazer a definição de um "nome" de coluna diferente.
    
    nome = Column(String(140))
    cpf = Column(String(14), unique=True)
    birthdate = Column(String(10))
    flight = Column(String(8))
    data_insercao = Column(DateTime, default=datetime.now())

    # A data de inserção será o instante de inserção caso não tenha
    # um valor definido pelo usuário
    data_insercao = Column(DateTime, default=datetime.now())

   
    # Estabelecendo o relacionamento entre produto e comentários
    contatos = relationship("Contato")

    def __init__(self, nome:str, cpf:str, flight:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Passageiro

        Arguments:
            nome: nome do passageiro.
            cpf: CPF do passageiro
            birthdate: data de nascimento do passageiro
            peso: peso do passageiro
            data_insercao: data de quando o passageiro foi inserido à base
        """
        self.nome = nome
        self.cpf = cpf
        self.birthdate
        self.flight = flight

       # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_contato(self, contato:Contato):
        """ Adiciona um novo Contato do Passageiro
        """
        self.contatos.append(contato)
