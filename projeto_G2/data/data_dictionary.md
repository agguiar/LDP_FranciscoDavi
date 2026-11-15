# Dicionário de Dados

## Projeto
Análise da Evolução dos Incidentes de Segurança Cibernética no Brasil entre 2010 e 2019.

## Descrição do conjunto de dados
O conjunto de dados contém registros mensais de incidentes
de segurança da informação reportados ao CERT.br,
abrangendo o período de janeiro de 2010 a dezembro de 2019.

## Fonte dos dados
CERT.br — Centro de Estudos, Resposta e Tratamento
de Incidentes de Segurança no Brasil.

Site: https://www.cert.br/

## Características gerais

- Período: 2010 a 2019
- Quantidade de registros: 120
- Quantidade de colunas originais: 10
- Quantidade de colunas processadas: 12
- Granularidade: mensal
- Valores ausentes identificados: 0
- Registros duplicados identificados: 0

## Descrição das variáveis

| Variável | Tipo | Descrição | Formato |
|---|---|---|---|
| Ano | int64 | Ano de referência dos registros | AAAA |
| Mes | string | Nome do mês de referência | Texto |
| Total | int64 | Total de incidentes registrados no mês | Inteiro |
| Worm | int64 | Incidentes classificados como worms | Inteiro |
| DOS | int64 | Incidentes classificados como negação de serviço | Inteiro |
| Invasao | int64 | Incidentes classificados como invasões | Inteiro |
| Web | int64 | Incidentes relacionados a ataques a servidores Web | Inteiro |
| Scan | int64 | Incidentes classificados como varreduras de redes | Inteiro |
| Fraude | int64 | Incidentes classificados como fraudes | Inteiro |
| Outros | int64 | Incidentes classificados em outras categorias | Inteiro |
| Numero_Mes | int64 | Representação numérica do mês | 1 a 12 |
| Data | datetime64 | Data de referência do registro mensal | AAAA-MM-DD |

## Tratamento dos dados

O processamento foi realizado utilizando Python e Pandas.

Etapas executadas:

1. Leitura do arquivo original com codificação UTF-8-SIG.
2. Identificação das colunas e tipos de dados.
3. Verificação de valores ausentes.
4. Verificação de registros duplicados.
5. Identificação do período analisado.
6. Conversão dos nomes dos meses para números.
7. Criação da coluna Data.
8. Ordenação cronológica dos registros.
9. Exportação dos dados tratados para CSV.

## Arquivos

### Dados originais
data/raw/cert_2010-2019.xls

### Dados processados
data/processed/incidentes_tratados.csv

## Reprodutibilidade

Para reproduzir o processamento, execute:

python src/etl.py

## Observações

O arquivo original foi preservado sem alterações.

A coluna Data utiliza o primeiro dia de cada mês
apenas como referência temporal para a análise.

Os valores representam incidentes reportados ao CERT.br
e não necessariamente todos os incidentes ocorridos no Brasil.