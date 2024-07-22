import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df = pd.read_csv("CLEAN_FIFA23_official_data.csv")
    df = df[df["Contract Valid Until"] >= datetime.today().year]
    df = df[df["Value(£)"] > 0]
    df = df.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df 
    
st.markdown("# FIFA23 OFFICIAL DATASET")

button = st.button("Acesse os Dados no Kaggle")

if button:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    """
    O conjunto de dados 
    dos jogadores em 2023.
    O conjunto de dados contém uma ampla game de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e afiliações de clubes.
    """
)