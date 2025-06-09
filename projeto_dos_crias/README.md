📚 StudyMatch – Backend
✅ Requisitos

- Python 3.8 ou superior
- pip instalado

🛠️ Instalação
Clone o repositório:

git clone https://github.com/motta1264/A2-Eng-Software.git

comandos iniciais:

- cd projeto_dos_crias
- pip install -r requirements.txt

▶️ Como rodar a aplicação

💻 macOS / Linux:

- export PYTHONPATH=.
- python app/main.py

🪟 Windows (CMD):

- set PYTHONPATH=.
- python app/main.py

🟦 Windows (PowerShell):

- $env:PYTHONPATH="."
- python app/main.py


## ✅ Checklist de Requisitos - Trabalho A2 (Arquitetura e Projeto de Software)

### 🎯 Objetivo e Tema
- [x] Aplicação web funcional com proposta realista (StudyMatch)
- [x] Solução de um problema concreto: organização de grupos de estudo

### 💻 Tecnologias Utilizadas
- [x] Python
- [x] Flask
- [x] SQLite
- [x] HTML/CSS (Jinja2 + Estilização personalizada)
- [x] Pytest (testes automatizados)
- [x] Git + GitHub

### 🧱 Arquitetura e Organização
- [x] Separação clara por camadas (Clean Architecture)
  - `domain/` – Entidades (User, Group, Task)
  - `use_cases/` – Regras de negócio
  - `infra/` – Repositórios com SQLite
  - `app/routes/` – Interface web (Flask)
  - `templates/` – Front-end (HTML)
  - `static/` – Estilo (CSS)
- [x] Organização compatível com estrutura recomendada no PDF

### 🧠 Princípios de Projeto
- [x] Aplicação dos princípios SOLID
  - Responsabilidade única nas entidades e use cases
  - Camadas desacopladas com injeção de dependências nos testes
- [x] Aplicação extensível e modular

### 🧪 Testes Automatizados
- [x] Testes de unidade nos use cases com repositórios simulados (sem dependência de banco)
- [x] Testes das entidades em `tests/domain`
- [x] Pytest configurado corretamente

### 📋 Funcionalidades Implementadas
- [x] Cadastro e login de usuários
- [x] Criação e exclusão de grupos
- [x] Participação em grupos
- [x] Pesquisa de grupos (com filtro de estilo)
- [x] Personalização de perfil do usuário
- [x] Visualização e listagem de grupos criados e grupos que participa

### 📐 Padrões e Estilo
- [x] Código seguindo convenções da PEP-8
- [x] Projeto executável localmente via `python app/main.py`
- [x] Diretivas `PYTHONPATH` documentadas

### ✅ Conclusão
- [x] Todos os requisitos do trabalho foram implementados e atendidos
- [x] Pronto para entrega e apresentação final
