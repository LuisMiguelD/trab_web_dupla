# Sistema de Gerenciamento de Tarefas - CRUD

## 📋 Sobre o Projeto

Sistema web desenvolvido para gerenciamento de tarefas com operações completas de CRUD (Create, Read, Update, Delete). Permite adicionar, visualizar, editar e excluir tarefas com controle de prioridades e status.

## 🚀 Tecnologias Utilizadas

### Backend
- **Python 3.x** - Linguagem de programação
- **Flask** - Framework web minimalista
- **SQLite** - Banco de dados relacional leve

### Frontend
- **HTML5** - Estrutura semântica das páginas
- **CSS3** - Estilização e responsividade

## 📂 Estrutura do Projeto

```
projeto_crud/
│
├── static/
│   ├── style.css          # Estilos e cores das prioridades
│   └── script.js          # Validações frontend (opcional)
│
├── templates/
│   ├── index.html         # Lista de tarefas (READ/DELETE)
│   ├── adicionar.html     # Formulário de criação (CREATE)
│   └── editar.html        # Formulário de edição (UPDATE)
│
├── app.py                 # Servidor Flask e rotas
├── criar_banco.py         # Script de inicialização do banco
├── banco.db               # Banco de dados SQLite
└── README.md              # Documentação
```

## 💾 Estrutura do Banco de Dados

O banco possui uma tabela `tarefas` com os seguintes campos:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Identificador único (chave primária) |
| titulo | TEXT | Título da tarefa (obrigatório) |
| descricao | TEXT | Descrição detalhada |
| data_criacao | DATETIME | Data de criação automática |
| data_vencimento | DATE | Data limite para conclusão |
| prioridade | TEXT | Baixa, Média ou Alta |
| status | TEXT | Pendente, Em Andamento ou Concluída |

## 🔧 Instalação e Configuração

### Pré-requisitos
- Python 3.7 ou superior instalado
- pip (gerenciador de pacotes Python)

### Passo 1: Clone ou baixe o projeto
```bash
git clone <url-do-repositorio>
cd projeto_crud
```

### Passo 2: Instale as dependências
```bash
pip install flask
```

### Passo 3: Crie o banco de dados
```bash
python criar_banco.py
```
Este comando irá gerar o arquivo `banco.db` com a estrutura necessária.

### Passo 4: Execute o servidor
```bash
python app.py
```

### Passo 5: Acesse no navegador
Abra seu navegador e acesse:
```
http://localhost:5000
```

## 📱 Funcionalidades

### ✅ CREATE - Adicionar Tarefa
- Acesse a página "Adicionar Tarefa"
- Preencha os campos:
  - **Título** (obrigatório)
  - **Descrição**
  - **Data de Vencimento**
  - **Prioridade** (Baixa, Média, Alta)
- Clique em "Salvar"

### 📖 READ - Visualizar Tarefas
- Na página inicial, veja todas as tarefas cadastradas
- Tarefas exibidas com cores diferentes conforme a prioridade:
  - 🟢 **Verde** - Prioridade Baixa
  - 🟡 **Amarelo** - Prioridade Média
  - 🔴 **Vermelho** - Prioridade Alta

### ✏️ UPDATE - Editar Tarefa
- Clique no botão "Editar" na tarefa desejada
- Modifique os campos necessários
- Atualize o status (Pendente, Em Andamento, Concluída)
- Clique em "Atualizar"

### 🗑️ DELETE - Excluir Tarefa
- Clique no botão "Excluir" na tarefa desejada
- Confirme a exclusão na mensagem que aparecer
- A tarefa será removida permanentemente

## 🎨 Recursos de Interface

- ✨ Design responsivo (funciona em mobile e desktop)
- 🎯 Indicadores visuais de prioridade por cores
- 📊 Organização clara das informações
- ⚡ Validação de formulários
- 🔒 Confirmação antes de exclusões

## 🛡️ Segurança

O sistema implementa:
- Validação de dados no backend
- Proteção contra SQL Injection (uso de queries parametrizadas)
- Tratamento de erros adequado

## 📝 Exemplos de Uso

### Exemplo 1: Criar uma tarefa urgente
1. Acesse "Adicionar Tarefa"
2. Título: "Entregar relatório mensal"
3. Descrição: "Relatório de vendas do mês de novembro"
4. Data de Vencimento: 30/11/2024
5. Prioridade: Alta
6. Salvar

### Exemplo 2: Atualizar status de tarefa
1. Na lista de tarefas, localize a tarefa
2. Clique em "Editar"
3. Altere o Status para "Em Andamento"
4. Clique em "Atualizar"

### Exemplo 3: Excluir tarefa concluída
1. Localize a tarefa concluída
2. Clique em "Excluir"
3. Confirme a ação

## 🐛 Solução de Problemas

### Erro ao executar app.py
- Certifique-se de que o Flask está instalado: `pip install flask`
- Verifique se está na pasta correta do projeto

### Banco de dados não encontrado
- Execute novamente: `python criar_banco.py`
- Verifique se o arquivo `banco.db` foi criado

### Porta 5000 já em uso
- Altere a porta no arquivo `app.py`:
  ```python
  app.run(debug=True, port=5001)
  ```

## 👥 Autores

- Ana Cristina Moreira Silva
- Luis Miguel De Sousa De Castro

## 📅 Data de Entrega

27/11/2024

## 📄 Licença

Projeto desenvolvido para fins educacionais - Atividade de CRUD.

---

**Observação:** Este projeto foi desenvolvido como atividade acadêmica seguindo os requisitos estabelecidos no documento "Projeto CRUD: Sistema de Gerenciamento".