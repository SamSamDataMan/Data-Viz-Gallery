import streamlit as st

def render_option():
    st.sidebar.title("Selection")
    option = st.sidebar.selectbox(
        "Page Navigation:",
        (
            "NBA Player Stats",
        ),
    )
    return option

def render_nba_player_stats_options(title, cols):
    variable = st.sidebar.selectbox('Choose your ' + title + ' Variable', cols[2:])
    return variable
