# Sessions

Uma aplicação web simples feita com **Flask** que implementa um sistema de **login de usuários** utilizando **sessões**. O projeto serve como base para autenticação e gerenciamento de usuários, usando `Flask-WTF` para os formulários e `Flask-SQLAlchemy` para o banco de dados.

## ✨ Funcionalidades

- Cadastro de usuário com nome, e-mail e senha (com hash).
- Login com validação de email e senha.
- Sessões para manter o usuário logado.
- Logout que encerra a sessão.
- Proteção contra CSRF com Flask-WTF.
- Validação de e-mails com `email-validator`.
- Interface simples com Bootstrap.

## 🛠 Tecnologias

- Python 3.13+
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Python-Dotenv
- Email-validator


## 🚀 Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/sessions.git
cd sessions

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

poetry install

FLASK_APP=src/sessions
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta

flask run
```