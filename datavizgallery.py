import os
import random
from re import M
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
from home import render_home
from sidebar import render_option, render_year_selection, optional_variable_checkbox, render_nba_player_stats_options

print('imports done')

option = render_option()

base = os.path.dirname(__file__)

if option == 'Home':
    render_home()
elif option == 'NBA':
    df = pd.read_csv(os.path.join(base, 'Data', 'NBA', 'Player Stats.csv'))
    df.rename(columns={"'+/-": "+/-"})
    cols = list(df.columns)

    year = render_year_selection(df)
    df = df[df['YEAR'] == year]

    # Choose Input Variables
    x_axis = render_nba_player_stats_options('X-Axis', cols, 15)
    y_axis = render_nba_player_stats_options('Y-Axis', cols, 16)
    markersize = optional_variable_checkbox('marker size')
    if markersize:
        size = render_nba_player_stats_options('Size', cols, 0)
    else:
        size = None

    # Define annotations dataframe
    x_head = df.sort_values(by=[x_axis], ascending=[False]).head(15)
    y_head = df.sort_values(by=[y_axis], ascending=[False]).head(15)
    annotations = pd.concat([x_head[['PLAYER', x_axis, y_axis]], y_head[['PLAYER', x_axis, y_axis]]]).drop_duplicates()

    st.title('Player Stats by Season')

    # Create Plot
    fig = plt.figure(figsize=(9, 9))
    plt.title(x_axis + ' vs ' + y_axis + ' Over ' + year + ' Season')
    ax = sns.scatterplot(x_axis,
                         y_axis,
                         data=df,
                         size=size,
                         color='#E47041',
                         edgecolor='black'
                         )
    plt.legend(prop={'size': 9})
    for i in range(len(annotations)):
        plt.annotate(annotations['PLAYER'].iloc[i],
                     (annotations[x_axis].iloc[i] + (annotations[x_axis].iloc[i] * 0.01),
                     (annotations[y_axis].iloc[i] + (annotations[y_axis].iloc[i] * (random.randrange(-2, 2) / 100)))))
    ax.set_facecolor('#c39c76')
    ax.set_axisbelow(True)
    plt.grid(b=True, which="major", linewidth=.5, color='#ffffff')
    st.pyplot(fig)

    st.write('Data Source: https://www.nba.com/stats')
