import pandas as pd
import streamlit as st

st.header("**Individual Team View**", divider='gray')

df = pd.read_csv("data/total_points.csv", index_col=[0])

col1, col2 = st.columns(2)
with col1:
    st.text("Select a Manager: ") 
    option = st.selectbox('Select a Manager',
                          sorted(df['Manager'].unique()),
                          label_visibility="collapsed")
    
with col2:
    st.text('Total Points: ')
    df2 = df.groupby(['Manager']).sum('Total Points').reset_index() 
    st.metric("Total Points", 
              round(df2[df2["Manager"] == option]["Total Points"].values[0], 2),
              label_visibility="collapsed")

st.divider()

df1 = df[df["Manager"] == option].loc[:, df.columns != 'Manager']

col_order = ['Team', 'Player', 'Total Points', 'Total Wildcard', 'Total Division', 'Total Conference', 'Total Superbowl']
df1 = df1[col_order]

st.dataframe(df1, hide_index=True, height=550, use_container_width=True)
