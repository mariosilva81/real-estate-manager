<p align="center">
  <a href="https://www.djangoproject.com" target="blank"><img src="https://cdn.worldvectorlogo.com/logos/django.svg" width="100" alt="Django Logo" /></a>
</p>

# Real Estate Manager

## Descrição

Este é um projeto de aplicação web desenvolvido em Django para facilitar o controle de locação de imóveis. O sistema permite o gerenciamento de imóveis, clientes e contratos de locação.

## Autor

Mario Silva

## Versão

1.0.0

## Principais Recursos

1. **Gerenciamento de Imóveis:** Registre informações abrangentes sobre cada propriedade, incluindo valor do aluguel, endereço, tipo de imóvel e fotos.

2. **Gestão de Clientes:** Armazene detalhes do cliente, incluindo nome, e-mail e telefone.

3. **Contratos de Locação:** Registre contratos de locação, especificando datas de início e término, valores de aluguel.

4. **Painel Administrativo:** Um painel administrativo para exibir e realizar a gestão dos dados.

## Tecnologias Utilizadas

<div style="display: flex;">
  <img src="https://cdn.worldvectorlogo.com/logos/django.svg" height="50" alt="Django" style="margin-right: 10px;">
</div>

## Dependências

Vide arquivo `requirements.txt` na raiz do projeto.

## Instalação

1. Clone o repositório: 

```bash
git clone git@github.com:mariosilva81/real-estate-manager.git
```

2. Navegue até o diretório do projeto.

3. Execute o seguinte comando para criar um ambiente virtual:

```
python -m venv venv
```

Se você estiver usando o Python 3.3 ou 3.4, pode ser necessário instalar a ferramenta venv separadamente usando pip install virtualenv.

4. Ative o ambiente virtual:

No Windows:

```
venv\Scripts\activate
```

No MacOS/Linux:

```
source ven/bin/activate
```

Quando o ambiente virtual estiver ativo, o prompt de comando mudará para mostrar o nome do ambiente.

5. Instale as dependências:

```
pip install -r requirements.txt
```

6. Crie e Aplique as Migrações:

```bash
# Cria as migrações
python manage.py makemigrations

# Aplica as migrações
python manage.py migrate
```

## Criando Usuário Admin

No Django, um "superuser" é um usuário com permissões administrativas que pode acessar a interface administrativa do Django, também conhecida como Django Admin. Para criar um superuser, você pode seguir estes passos:

1. **Execute o comando `createsuperuser`:**

Abra um terminal, vá para o diretório do seu projeto Django e execute o seguinte comando:

```bash
python manage.py createsuperuser
```

Dependendo da configuração do seu ambiente, você também pode usar `python3` em vez de `python`.

2. **Preencha as informações do superuser:**

O comando `createsuperuser` solicitará que você preencha algumas informações, como nome de usuário, endereço de e-mail e senha para o novo superuser.

```bash
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********
```

Substitua "admin" e "admin@example.com" pelos detalhes desejados para o seu superuser.

3. **Confirme o sucesso:**

Depois de preencher as informações solicitadas, você receberá uma mensagem confirmando que o superuser foi criado com sucesso.

```bash
Superuser created successfully.
```

Acesse a interface administrativa em `http://localhost:8000/admin/`.

## Executando o Projeto

Execute o seguinte comando para iniciar o servidor:

```
python manage.py runserver
```

A aplicação estará acessível localmente em [http://localhost:8000](http://localhost:8000). 

Se precisar especificar uma porta diferente, você pode fornecer o número da porta como argumento para o comando runserver, por exemplo:

```
python manage.py runserver 8080
```

## Contato

Para questões ou sugestões, entre em contato através do email: mariosilva.81@icloud.com.
