import streamlit as st
import pandas as pd

st.header("**Scoreboard**", divider='gray')

if "df" not in st.session_state:
    st.session_state.df = pd.read_csv("data/managers_games.csv", index_col=[0])

if "total_points_df" not in st.session_state:
    st.session_state.total_points_df = pd.read_csv("data/total_points.csv", index_col=[0])


df1 = st.session_statedf.groupby('Manager')["Division"].sum().reset_index(name='Players Remaining')

df2 = st.session_state.total_points_df.groupby(['Manager']).sum('Total Points')  #.reset_index()
df2 = df2.merge(df1, on='Manager').sort_values(by='Total Points', ascending=False) 

col_order = ['Manager', 'Players Remaining', 'Total Points', 'Total_WC', 'Total_Div', 'Total_Conf', 'Total_SB']
df2 = df2[col_order]

st.dataframe(df2, hide_index=True, height=750, use_container_width=True)
