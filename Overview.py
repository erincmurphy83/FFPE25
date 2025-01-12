import streamlit as st

st.set_page_config(page_title="Fantasy Football Playoff Edition", page_icon="🏈", layout="wide", initial_sidebar_state="expanded")
st.header("**Fantasy Football Playoff Edition**", divider='gray')
# st.sidebar.markdown("# Team Selection")

images = ["images/players.jpg", "images/points_25.png"]
captions = ["Available players", "Scoring system."]

# st.image(images, caption=captions, use_column_width=True)

col1, col2 = st.columns(2)

with col1:
    st.image(images[0], captions[0])

with col2:
    st.image(images[1], captions[1])




# streamlit run Playoff_Football_Dashboard/Overview.py
