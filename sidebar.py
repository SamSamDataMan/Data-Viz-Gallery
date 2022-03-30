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

def render_option_nba():
    st.sidebar.title("NBA Chart Options:")
    option_nba = st.sidebar.selectbox(
        'NBA Charts:',
        (
            # 'Year to Year Comparison',
            'Single Season Multi-Stat Comparison',
        ),
    )
    return option_nba

def optional_variable_checkbox(function):
    return st.sidebar.checkbox(f'Add a {function} variable?')

def render_year_selection(df):
    year = st.sidebar.selectbox('Choose an NBA Season', list(df.YEAR.unique()), 0)
    return year

def render_nba_player_stats_options(title, cols, default):
    variable = st.sidebar.selectbox('Choose your ' + title + ' Variable', cols[4:], index=default)
    return variable

def bigger_chart():
    return st.sidebar.checkbox('Help! Labels are overlapping!')

def even_bigger_chart():
    return st.sidebar.checkbox('Help! Labels still are overlapping!')
