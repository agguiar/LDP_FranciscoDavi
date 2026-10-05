import streamlit as st

st.set_page_config(
    page_title="Sobre o projeto",
    layout="wide"
)

st.title("Sobre o projeto")

st.markdown("""
**Disciplina:** Linguagens de Programação  
**Professor:** Alexandre Neves Louzada  
**Aluno:** Francisco Davi Barreto Aguiar
""")

st.header("Objetivo")

st.write(
    "Analisar uma base simulada de criminalidade, explorando "
    "a evolução das ocorrências e as diferenças entre cidades, "
    "regiões, tipos de crime e períodos do dia."
)

st.header("Base de dados")

st.write(
    "A base original contém 4.440 registros de 37 cidades "
    "brasileiras, entre janeiro de 2015 e dezembro de 2024. "
    "Inclui ocorrências, vítimas, prisões, renda média, "
    "índice de violência e nível de risco."
)

st.header("Metodologia")

st.markdown("""
- Leitura e tratamento dos dados com Pandas.
- Verificação de valores ausentes, duplicados e datas.
- Criação de campos de ano e mês, nome do mês e trimestre.
- Cálculo de indicadores e agrupamentos.
- Visualização com Matplotlib e Seaborn.
- Análise de correlação de Pearson.
- Armazenamento em SQLite utilizando SQLAlchemy no notebook.
- Construção do dashboard com Streamlit.
""")

st.header("Como interpretar")

st.write(
    "Os rankings de cidades e crimes utilizam a soma das "
    "ocorrências. A comparação do índice de violência utiliza "
    "a média dos valores disponíveis. A participação percentual "
    "representa a parcela das ocorrências no total filtrado."
)

st.header("Limitações")

st.write(
    "Os dados são simulados e não representam a segurança real "
    "das cidades. Os totais não são ajustados pela população. "
    "A fórmula do índice de violência não foi informada, "
    "e a correlação não comprova causa e efeito."
)
