import pandas as pd
import streamlit as st

st.header("**Individual Team**", divider='gray')

if "df" not in st.session_state:
    st.session_state.df = pd.read_csv("Playoff_Football_Dashboard/data/managers_games.csv", index_col=[0])


col1, col2 = st.columns(2)
with col1:
    option = st.selectbox("Who's team do you wish to see",
                          sorted(st.session_state.df['Manager'].unique()))
with col2:
    st.text('Total Points: ')
    # st.write(st.session_state.df[st.session_state.df["Manager"] == option].sum()["Points"])

st.divider()

df1 = st.session_state.df[st.session_state.df["Manager"] == option].loc[:, st.session_state.df.columns != 'Manager']

st.dataframe(df1, hide_index=True, height=500)