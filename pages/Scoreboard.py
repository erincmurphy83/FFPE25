import streamlit as st
import pandas as pd

st.header("**Scoreboard**", divider='gray')

df1 = pd.read_csv("data/managers_games.csv", index_col=[0])   
total_points_df = pd.read_csv("data/total_points.csv", index_col=[0])

df1 = df1.groupby('Manager')["Conference"].sum().reset_index(name='Players Remaining')
df2 = total_points_df.groupby(['Manager']).sum('Total Points').round(2)  #.reset_index()
df2 = df2.merge(df1, on='Manager').sort_values(by='Total Points', ascending=False) 

# Add a ranking column based on 'Total Points'
df2['Rank'] = df2['Total Points'].rank(method='max', ascending=False).astype(int)

# Reorder the columns
col_order = ['Rank', 'Manager', 'Players Remaining', 'Total Points', 'Total Wildcard', 'Total Division', 'Total Conference', 'Total Superbowl']
df2 = df2[col_order]

st.dataframe(df2, hide_index=True, height=750, use_container_width=True)
