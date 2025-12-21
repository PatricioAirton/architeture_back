 # Aplicação backend com chamada pra uma API Externa

Este projeto faz parte do MVP que incrementa o trabalho apresentado na Sprint Desenvolvimento full stack que suporta uma aplicação web para o gerenciamento de passageiros de um voo de eVTOL.

Para efeitos desse MVP, optou-se pelo cenário 1.1 com uma chamada de uma api externa a partir do backend.

A api externa selecionada verifica e valida a situação de um CPF junto à Receita Federal o que torna possível a correta identificação do passageiro e sua inclusão na lista de passageiros.

# Arquitetura da solução

Com base nos cenários sugeridos na sprint de aquitetura de software e na necessidade de containerização da aplicação utilizando o docker como requisito para a implementação, a solução foi projetada de acordo com a imagem abaixo:

!(architecture_back/aquitetura_mvp.png)


O objetivo aqui é apresetar uma API emplementada seguindo o estilo REST.

As principais tecnologias que serão utilizadas aqui é o:
 - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
 - [SQLAlchemy](https://www.sqlalchemy.org/)
 - [OpenAPI3](https://swagger.io/specification/)
 - [SQLite](https://www.sqlite.org/index.html)

---
### Instalação


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

---
### Executando o servidor


Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5002
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 
#
```
(env)$ flask run --host 0.0.0.0 --port 5002 --reload
```

---
### Acesso no browser

Abra o [http://localhost:5002/#/](http://localhost:5002/#/) no navegador para verificar o status da API em execução.

---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t rest-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5002:5002 rest-api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5002/#/](http://localhost:5001/#/) no navegador.



### Alguns comandos úteis do Docker

>**Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
>```
>$ docker images
>```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>```
>$ docker rmi <IMAGE ID>
>```
>Subistituindo o `IMAGE ID` pelo código da imagem
>
>**Para verificar se o container está em execução** você pode executar o seguinte comando:
>
>```
>$ docker container ls --all
>```
>
> Caso queira **parar um container**, basta executar o comando:
>```
>$ docker stop <CONTAINER ID>
>```
>Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
>
> Caso queira **destruir um container**, basta executar o comando:
>```
>$ docker rm <CONTAINER ID>
>```
>Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).