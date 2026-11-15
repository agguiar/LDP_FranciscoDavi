import pandas as pd
from pathlib import Path

caminho = Path(__file__).resolve().parent.parent / "data" / "raw" / "cert_2010-2019.xls"

dados = pd.read_csv(caminho, sep=";", encoding="utf-8-sig")

print("Primeiras linhas do conjunto de dados:")
print(dados.head())

print("\nDimensões do conjunto de dados:")
print(dados.shape)

print("\nNomes das colunas:")
print(dados.columns.tolist())

print("\nTipos de dados:")
print(dados.dtypes)

print("\nValores ausentes por coluna:")
print(dados.isnull().sum())

print("\nQuantidade de registros duplicados:")
print(dados.duplicated().sum())

print("\nPeríodo analisado:")
print("Ano inicial:", dados["Ano"].min())
print("Ano final:", dados["Ano"].max())

print("\nEstatísticas descritivas:")
print(dados.describe())

meses = {
    "Janeiro": 1,
    "Fevereiro": 2,
    "Março": 3,
    "Abril": 4,
    "Maio": 5,
    "Junho": 6,
    "Julho": 7,
    "Agosto": 8,
    "Setembro": 9,
    "Outubro": 10,
    "Novembro": 11,
    "Dezembro": 12
}

dados["Numero_Mes"] = dados["Mes"].map(meses)

if dados["Numero_Mes"].isnull().any():
    raise ValueError("Existem meses não reconhecidos.")

dados["Data"] = pd.to_datetime(
    dict(
        year=dados["Ano"],
        month=dados["Numero_Mes"],
        day=1
    )
)

dados = dados.sort_values("Data").reset_index(drop=True)

pasta_saida = caminho.parent.parent / "processed"
pasta_saida.mkdir(parents=True, exist_ok=True)

arquivo_saida = pasta_saida / "incidentes_tratados.csv"

dados.to_csv(
    arquivo_saida,
    index=False,
    encoding="utf-8-sig"
)

print("\nDados tratados com sucesso!")
print("\nPrimeiras linhas após o tratamento:")
print(dados.head())

print("\nArquivo salvo em:", arquivo_saida)
