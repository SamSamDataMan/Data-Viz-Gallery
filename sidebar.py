import streamlit as st

def render_option():
    st.sidebar.title("User Selections:")
    option = st.sidebar.selectbox(
        'Page Navigation:',
        (
            'Home',
            'NBA',
        ),
    )
    return option

def optional_variable_checkbox(function):
    return st.sidebar.checkbox(f'Add a {function} variable?')

def render_year_selection(df):
    year = st.sidebar.selectbox('Choose an NBA Season', ['2021-2022'], 0)
    return year

def render_nba_player_stats_options(title, cols, default):
    variable = st.sidebar.selectbox('Choose your ' + title + ' Variable', cols[4:], index=default)
    return variable
