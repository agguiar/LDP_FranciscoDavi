# Análise de Incidentes Cibernéticos no Brasil (2010–2019)

## Sobre o projeto

Este projeto apresenta uma análise exploratória das notificações de incidentes cibernéticos no Brasil entre 2010 e 2019, utilizando dados históricos do CERT.br.

O objetivo é identificar tendências temporais, examinar a distribuição dos incidentes por categoria e investigar as variações anuais nas notificações.

## Informações acadêmicas

- Autor: Francisco Davi Barreto Aguiar
- Curso: Bacharelado em Sistemas de Informação
- Período: 6º
- Disciplina: Linguagem de Programação — Análise e Visualização de Dados com Python

## Palavras-chave

Segurança da informação; Incidentes cibernéticos; CERT.br; Análise exploratória de dados; Python; Visualização de dados.

## Fonte dos dados

Os dados utilizados são provenientes das estatísticas de incidentes reportados ao CERT.br.

Fonte oficial: https://stats.cert.br/

Período analisado: 2010 a 2019.

## Metodologia

O projeto utiliza Python para realizar a leitura, o tratamento e a análise dos dados.

As etapas incluem:

1. Importação dos dados originais.
2. Tratamento e padronização das informações.
3. Verificação de valores ausentes e duplicados.
4. Organização dos dados processados.
5. Análise exploratória e geração de gráficos.
6. Publicação dos resultados em um artigo acadêmico HTML.

## Principais resultados

A base analisada contém 120 observações mensais, abrangendo o período de 2010 a 2019.

Foram contabilizadas 6.163.277 notificações de incidentes no período. O ano de 2014 apresentou o maior volume anual, enquanto 2010 apresentou o menor.

Os gráficos permitem examinar a evolução anual, as categorias de incidentes e as variações percentuais entre os anos.

## Estrutura do projeto

```text
projeto_G2/
├── data/
│   ├── raw/
│   ├── processed/
│   └── data_dictionary.md
├── docs/
│   ├── index.html
│   └── assets/
├── notebooks/
│   └── analise_exploratoria.ipynb
├── src/
│   ├── __init__.py
│   └── etl.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/agguiar/LDP_FranciscoDavi.git
cd LDP_FranciscoDavi/projeto_G2
```

Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o processamento dos dados:

```bash
python -m src.etl
```

Para explorar os resultados, abra o notebook `notebooks/analise_exploratoria.ipynb` em um ambiente Jupyter.

## Artigo acadêmico

O artigo completo, com metodologia, resultados e visualizações, está disponível em:

https://agguiar.github.io/LDP_FranciscoDavi/projeto_G2/docs/

## Princípios FAIR

- **Findable:** repositório público, documentação e identificação da fonte dos dados.
- **Accessible:** acesso público aos arquivos e ao artigo HTML.
- **Interoperable:** dados processados em CSV e dicionário de variáveis.
- **Reusable:** código-fonte, dependências documentadas e licença aberta.

## Licença

O código deste projeto será disponibilizado sob a licença MIT. Consulte o arquivo `LICENSE`.