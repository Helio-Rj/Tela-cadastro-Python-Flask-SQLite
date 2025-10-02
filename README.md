# Projeto Flask - Cadastro de Usuários

Este projeto é uma aplicação web simples desenvolvida com Flask, que permite cadastrar, listar, editar e excluir usuários utilizando um banco de dados SQLite.

## Funcionalidades
- Cadastro de usuários (nome e e-mail)
- Listagem de todos os usuários cadastrados
- Edição dos dados de um usuário
- Exclusão de usuários
- Feedback visual após cadastro

## Estrutura do Projeto
```
flask 1.0/
├── app.py                  # Código principal da aplicação Flask
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto
├── cadastro.db             # Banco de dados SQLite (gerado automaticamente)
├── static/
│   └── style.css           # Arquivo de estilos CSS
└── templates/
    ├── index.html          # Formulário de cadastro
    ├── sucesso.html        # Página de sucesso após cadastro
    └── lista.html          # Listagem de usuários
```

## Como Executar
1. **Instale o Python 3.x**
2. **Instale as dependências**:
   ```powershell
   pip install -r requirements.txt
   ```
3. **Execute a aplicação**:
   ```powershell
   python app.py
   ```
4. **Acesse no navegador**:
   - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Estrutura dos Templates
- `index.html`: Formulário para cadastro de novos usuários.
- `sucesso.html`: Exibe mensagem de sucesso e os dados cadastrados.
- `lista.html`: Mostra todos os usuários cadastrados, com opções de editar e excluir.

## Banco de Dados
- Utiliza SQLite, criado automaticamente ao iniciar o projeto.
- Tabela: `usuarios` (id, nome, email)

## Estilo Visual
- O arquivo `static/style.css` estiliza todos os formulários e tabelas para uma aparência moderna e responsiva.

## Requisitos
- Python 3.x
- Flask

## Observações
- O projeto é didático e pode ser expandido para incluir autenticação, validação avançada, paginação, etc.
- Para produção, recomenda-se configurar variáveis de ambiente e proteger rotas sensíveis.

## Licença
Este projeto é livre para uso educacional.
