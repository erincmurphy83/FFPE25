import streamlit as st
import pandas as pd

st.header("**Scoreboard**", divider='gray')

if "df" not in st.session_state:
    st.session_state.df = pd.read_csv("data/managers_games.csv", index_col=[0])

df1 = st.session_state.df.groupby('Manager').size().reset_index(name='Players Remaining')

st.dataframe(df1, hide_index=True, height=500)
