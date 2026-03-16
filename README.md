# Projeto ETL: Universidades (Hipolabs API) 🎓

Este projeto foi desenvolvido como atividade prática da aula de Engenharia de Dados. O objetivo é realizar um processo de ETL (Extract, Transform, Load) para extrair dados de universidades de diferentes países e armazená-los em um banco de dados SQLite.

## 👥 Integrantes do Grupo
- Dayanne Moraes
- Douglas Araújo
- Lucas Mateus

## 🛠️ Estrutura do Projeto
O projeto segue uma arquitetura modular para facilitar a manutenção e escalabilidade:

- **`src/`**: Pacote principal contendo os módulos de lógica.
  - **`extract.py`**: Classe `Extract` responsável por consumir a API.
  - **`load.py`**: Classe `Load` responsável pela criação do banco e inserção dos dados.
- **`main.py`**: Ponto de entrada que coordena o fluxo de ETL para múltiplos países (Brasil, China, França, Itália).
- **`universities.db`**: Banco de Dados SQLite gerado pelo processo.

## 📋 Requisitos Atendidos
- **Docstrings**: Todos os métodos possuem documentação clara sobre sua responsabilidade e argumentos.
- **Formatação (Black)**: O código foi padronizado utilizando a biblioteca `black`.
- **Arquitetura Modular**: Separação clara entre extração e carregamento de dados.

## 🚀 Como Executar
1. Certifique-se de ter o Python instalado.
2. Instale as dependências:
   ```bash
   pip install requests black
   ```
3. Execute o projeto:
   ```bash
   python main.py
   ```

*Este projeto foi formatado automaticamente via Black e segue as boas práticas de desenvolvimento em Python.*
