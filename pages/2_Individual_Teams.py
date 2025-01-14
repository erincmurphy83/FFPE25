import pandas as pd
import streamlit as st

st.header("**Individual Team**", divider='gray')

# if "df" not in st.session_state:
#     st.session_state.df = pd.read_csv("data/total_points.csv", index_col=[0])

df = pd.read_csv("data/total_points.csv", index_col=[0])

col1, col2 = st.columns(2)
with col1:
    st.text("Select a Manager: ")   

    option = st.selectbox('',
                          sorted(df['Manager'].unique()) )
with col2:
    st.text('Total Points: ')
    df2 = df.groupby(['Manager']).sum('Total Points').reset_index() 
    st.metric("", df2[df2["Manager"] == option]["Total Points"].values[0])

st.divider()

df1 = st.session_state.df[st.session_state.df["Manager"] == option].loc[:, st.session_state.df.columns != 'Manager']

col_order = ['Team', 'Player', 'Total Points', 'Total_WC', 'Total_Div', 'Total_Conf', 'Total_SB']
df1 = df1[col_order]

st.dataframe(df1, hide_index=True, height=550, use_container_width=True)
