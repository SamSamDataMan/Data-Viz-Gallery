import streamlit as st

def render_home():
    st.title('Data Visualization Gallery')
    st.subheader('By Sam King')
    st.text('Github | Twitter: @samsamdataman \n'
            'LinkedIn: www.linkedin.com/in/seking002')
    st.write('Welcome to Sam King\'s Data Visualization Gallery. Use the options in the side bar to navigate \n'
             'through the gallery, select filters, and choose inputs for each visualization.')
    if st.checkbox('Table of Contents'):
        with st.expander('NBA'):
            if st.checkbox('Player Stats by Season'):
                st.write('Player Stats by Season')
                st.write('Scatterplot plotting two user-selected stats against one another, with optional third variable for marker size')
                st.write('Notes: Data labels are available for top 10 players along each axis. Labels occassionally overlap, try reloading page to eliminate label collisions.')
                st.write('Data Source: Data Source: https://www.nba.com/stats')
        #     if st.checkbox('Dumbbell Charts'):
        #         st.write('pass')
        # with st.expander('Other Subject Area'):
        #     st.write('pass')
