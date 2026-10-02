import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import pandas as pd

st.set_page_config(
    page_title="Análise de Criminalidade",
    layout="wide"
)

st.title("Criminalidade em Grandes Cidades Brasileiras")

st.write(
    "Análise de dados simulados de criminalidade "
    "entre 2015 e 2024."
)


PASTA_PROJETO = Path(__file__).resolve().parent

@st.cache_data
def carregar_dados():
    caminho = PASTA_PROJETO / "dados" / "criminalidade_tratada.csv"
    return pd.read_csv(caminho, parse_dates=["data"])

df = carregar_dados()

st.sidebar.header("Filtros")

df_filtrado = df.copy()

filtros = [
    ("Ano", "ano"),
    ("Mês", "mes"),
    ("Região", "regiao"),
    ("Estado", "uf"),
    ("Cidade", "cidade"),
    ("Tipo de crime", "tipo_crime"),
    ("Nível de risco", "nivel_risco")
]

for titulo, coluna in filtros:
    opcoes = sorted(df_filtrado[coluna].dropna().unique().tolist())

    selecionado = st.sidebar.selectbox(
        titulo,
        ["Todos"] + opcoes,
        key=f"filtro_{coluna}"
    )

    if selecionado != "Todos":
        df_filtrado = df_filtrado[
            df_filtrado[coluna] == selecionado
        ]

if df_filtrado.empty:
    st.warning("Não há registros para os filtros selecionados.")
    st.stop()

st.subheader("Dados filtrados")
st.write(f"Registros encontrados: {len(df_filtrado)}")
tabela_exibicao = df_filtrado.rename(columns={
    "ano": "Ano",
    "mes": "Mês",
    "data": "Data",
    "regiao": "Região",
    "uf": "Estado (UF)",
    "cidade": "Cidade",
    "bairro": "Bairro",
    "tipo_crime": "Tipo de crime",
    "periodo_dia": "Período do dia",
    "ocorrencias": "Ocorrências",
    "vitimas": "Vítimas",
    "prisoes": "Prisões",
    "renda_media": "Renda média (R$)",
    "indice_violencia": "Índice de violência",
    "nivel_risco": "Nível de risco",
    "ano_mes": "Ano e mês",
    "nome_mes": "Nome do mês",
    "trimestre": "Trimestre"
}).copy()

tabela_exibicao["Data"] = (
    tabela_exibicao["Data"].dt.strftime("%d/%m/%Y")
)

st.dataframe(
    tabela_exibicao,
    hide_index=True,
    use_container_width=True
)

st.subheader("Indicadores do período selecionado")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total de ocorrências",
    f"{df_filtrado['ocorrencias'].sum():,.0f}".replace(",", ".")
)

col2.metric(
    "Total de vítimas",
    f"{df_filtrado['vitimas'].sum():,.0f}".replace(",", ".")
)

col3.metric(
    "Total de prisões",
    f"{df_filtrado['prisoes'].sum():,.0f}".replace(",", ".")
)

col4.metric(
    "Índice médio de violência",
    f"{df_filtrado['indice_violencia'].mean():.2f}".replace(".", ",")
)

ranking_cidades = (
    df_filtrado.groupby(["cidade", "uf"])["ocorrencias"]
    .sum()
    .sort_values(ascending=False)
)

ranking_crimes = (
    df_filtrado.groupby("tipo_crime")["ocorrencias"]
    .sum()
    .sort_values(ascending=False)
)

ranking_regioes = (
    df_filtrado.groupby("regiao")["indice_violencia"]
    .mean()
    .sort_values(ascending=False)
)

cidade, uf = ranking_cidades.index[0]

col5, col6, col7 = st.columns(3)

col5.metric(
    "Cidade com mais ocorrências",
    f"{cidade} / {uf}"
)

col6.metric(
    "Crime com mais ocorrências",
    ranking_crimes.index[0]
)

col7.metric(
    "Região com maior índice médio",
    ranking_regioes.index[0]
)

st.caption(
    "Indicadores da base simulada conforme os filtros. "
    "Em caso de empate, é exibido um dos líderes."
)

st.subheader("Evolução mensal das ocorrências")

evolucao_mensal = (
    df_filtrado.groupby("data")["ocorrencias"]
    .sum()
    .sort_index()
)

st.line_chart(evolucao_mensal)

st.caption(
    "O gráfico apresenta a soma das ocorrências por mês "
    "na base simulada, considerando o ano selecionado."
)

st.subheader("Ocorrências por tipo de crime")

ocorrencias_crime = (
    df_filtrado.groupby("tipo_crime")["ocorrencias"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(12, 5))

sns.barplot(
    x=ocorrencias_crime.index,
    y=ocorrencias_crime.values,
    color="steelblue",
    ax=ax
)

ax.set_xlabel("Tipo de crime")
ax.set_ylabel("Total de ocorrências")
ax.tick_params(axis="x", rotation=0)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.caption(
    "Os valores representam o total de ocorrências de cada "
    "tipo de crime no período selecionado."
)

st.subheader("Cidades com mais ocorrências")

top_cidades = (
    df_filtrado.groupby(["cidade", "uf"])["ocorrencias"]
    .sum()
    .nlargest(10)
    .reset_index()
)

top_cidades["cidade_uf"] = (
    top_cidades["cidade"] + " — " + top_cidades["uf"]
)

fig, ax = plt.subplots(figsize=(12, 6))

sns.barplot(
    data=top_cidades,
    x="ocorrencias",
    y="cidade_uf",
    color="steelblue",
    ax=ax
)

ax.set_xlabel("Total de ocorrências")
ax.set_ylabel("Cidade")

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.caption(
    "Ranking da base simulada considerando o filtro selecionado. "
    "Os totais não são ajustados pela população."
)

st.subheader("Comparação entre regiões")

resumo_regioes = (
    df_filtrado.groupby("regiao")
    .agg(
        total_ocorrencias=("ocorrencias", "sum"),
        media_por_registro=("ocorrencias", "mean"),
        indice_medio_violencia=("indice_violencia", "mean")
    )
    .sort_values("total_ocorrencias", ascending=False)
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    x=resumo_regioes["total_ocorrencias"],
    y=resumo_regioes.index,
    color="steelblue",
    ax=ax
)

ax.set_xlabel("Total de ocorrências")
ax.set_ylabel("Região")

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

tabela_regioes = resumo_regioes.copy()

tabela_regioes["participacao"] = (
    tabela_regioes["total_ocorrencias"]
    / tabela_regioes["total_ocorrencias"].sum()
    * 100
)

tabela_regioes = tabela_regioes.reset_index().rename(columns={
    "regiao": "Região",
    "total_ocorrencias": "Total de ocorrências",
    "media_por_registro": "Média de ocorrências por registro",
    "indice_medio_violencia": "Índice médio de violência",
    "participacao": "Participação nas ocorrências"
})

def formatar_numero(valor, casas=2):
    return (
        f"{valor:,.{casas}f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

st.dataframe(
    tabela_regioes.style.format({
        "Total de ocorrências": lambda v: formatar_numero(v, 0),
        "Média de ocorrências por registro": formatar_numero,
        "Índice médio de violência": formatar_numero,
        "Participação nas ocorrências": lambda v: (
            f"{formatar_numero(v)}%"
        )
    }),
    hide_index=True,
    use_container_width=True
)

st.caption(
    "As regiões têm diferentes quantidades de cidades na base. "
    "A média por registro complementa os totais, "
    "mas não representa uma taxa por habitante."
)

st.subheader("Ocorrências por crime e período do dia")

mapa_calor = df_filtrado.pivot_table(
    index="tipo_crime",
    columns="periodo_dia",
    values="ocorrencias",
    aggfunc="sum",
    fill_value=0
).reindex(
    columns=["Madrugada", "Manhã", "Tarde", "Noite"],
    fill_value=0
)

fig, ax = plt.subplots(figsize=(10, 6))

sns.heatmap(
    mapa_calor,
    annot=True,
    fmt=".0f",
    cmap="YlOrRd",
    linewidths=0.5,
    cbar_kws={"label": "Total de ocorrências"},
    ax=ax
)

ax.set_xlabel("Período do dia")
ax.set_ylabel("Tipo de crime")
ax.tick_params(axis="x", rotation=0)
ax.tick_params(axis="y", rotation=0)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.caption(
    "As cores mais escuras indicam maiores totais de ocorrências "
    "nos filtros selecionados. Zero indica ausência de "
    "ocorrências registradas nessa combinação na base filtrada."
)

st.subheader("Renda média e índice de violência")

fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df_filtrado,
    x="renda_media",
    y="indice_violencia",
    hue="regiao",
    alpha=0.7,
    ax=ax
)

ax.set_xlabel("Renda média (R$)")
ax.set_ylabel("Índice de violência")
ax.legend(title="Região")

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

dados_correlacao = df_filtrado[
    ["renda_media", "indice_violencia"]
].dropna()

if (
    len(dados_correlacao) >= 3
    and dados_correlacao["renda_media"].nunique() > 1
    and dados_correlacao["indice_violencia"].nunique() > 1
):
    correlacao = dados_correlacao["renda_media"].corr(
        dados_correlacao["indice_violencia"]
    )

    st.write(
        f"Correlação de Pearson: {correlacao:.3f}"
        .replace(".", ",")
    )
else:
    st.info(
        "Os filtros selecionados não fornecem dados suficientes "
        "com variação para calcular a correlação."
    )

st.caption(
    "Cada ponto representa um registro da base filtrada. "
    "A correlação varia de -1 a 1 e não é uma porcentagem. "
    "Essa relação na base simulada não demonstra causa e efeito."
)

st.subheader("Ocorrências por região e tipo de crime")

tabela_crimes = df_filtrado.pivot_table(
    index="regiao",
    columns="tipo_crime",
    values="ocorrencias",
    aggfunc="sum",
    fill_value=0,
    margins=True,
    margins_name="Total"
)

tabela_crimes.index.name = "Região"
tabela_crimes.columns.name = "Tipo de crime"

st.dataframe(
    tabela_crimes.style.format(
        lambda valor: f"{valor:,.0f}".replace(",", ".")
    ),
    use_container_width=True
)

st.caption(
    "A tabela apresenta os totais de ocorrências por região "
    "e tipo de crime, considerando os filtros selecionados."
)

st.subheader("Análise dos resultados")

st.write(
    f"Nos filtros selecionados, {cidade} / {uf} apresenta "
    f"o maior total de ocorrências, com "
    f"{int(ranking_cidades.iloc[0]):,} registros de ocorrências. "
    f"O crime com maior total é o {ranking_crimes.index[0]}. "
    f"A região com maior índice médio de violência é o "
    f"{ranking_regioes.index[0]}, com "
    f"{ranking_regioes.iloc[0]:.2f}."
)


st.subheader("Conclusão")

st.write(
    "O projeto transformou os dados de criminalidade em informações "
    "visuais, permitindo acompanhar a evolução das ocorrências e "
    "comparar cidades, regiões, tipos de crime e períodos do dia. "
    "Os filtros e indicadores facilitam a exploração dos dados, "
    "enquanto a análise de correlação investiga a relação entre "
    "renda média e índice de violência."
)

st.write(
    "Como a base é simulada, os resultados demonstram a aplicação "
    "das ferramentas de análise, sem representar a segurança real "
    "das cidades. As comparações utilizam totais sem ajuste pela "
    "população, e a correlação não comprova causa e efeito."
)