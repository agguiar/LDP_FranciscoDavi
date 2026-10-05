# Criminalidade em Grandes Cidades Brasileiras

Projeto acadêmico de análise e visualização de dados com Python.

**Disciplina:** Linguagens de Programação  
**Professor:** Alexandre Neves Louzada  
**Aluno:** Francisco Davi Barreto Aguiar

## Objetivo

Explorar a evolução das ocorrências e comparar cidades, regiões,
tipos de crime e períodos do dia por meio de um dashboard interativo.

## Base de dados

Base simulada com 4.440 registros de 37 cidades brasileiras,
entre janeiro de 2015 e dezembro de 2024.

Fonte: Alexandre Louzada — repositório Dados-Simulados-G2.
https://github.com/AlexandreLouzada/Dados-Simulados-G2

## Tecnologias

- Python e Pandas
- Matplotlib e Seaborn
- Streamlit
- SQLAlchemy e SQLite

## Funcionalidades

- Filtros por ano, mês, região, estado, cidade, crime e risco.
- Indicadores atualizados conforme os filtros.
- Evolução mensal das ocorrências.
- Rankings de cidades e tipos de crime.
- Comparação regional.
- Mapa de calor por crime e período do dia.
- Gráfico de renda média e índice de violência.
- Correlação de Pearson.
- Tabela de ocorrências por região e crime.
- Página com metodologia e limitações.
- Tratamento e armazenamento em SQLite no notebook.

## Pastas e arquivos

- Dashboard.py: aplicação principal.
- pages/: página sobre o projeto.
- dados/: bases original e tratada.
- db/: banco SQLite.
- ntb/: notebook de análise.
- imagens/: imagens do projeto.
- requirements.txt: dependências.

## Como executar no Windows

Execute os comandos na pasta do projeto:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run Dashboard.py
```

## Limitações

Os dados são simulados e não representam a segurança real das cidades.
Os totais não são ajustados pela população, e as regiões possuem
quantidades diferentes de cidades na base.

O índice de violência não é uma porcentagem e sua fórmula não foi
informada. A correlação não comprova causa e efeito.
