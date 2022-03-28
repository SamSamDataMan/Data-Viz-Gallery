import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
from sidebar import render_option, render_nba_player_stats_options

option = render_option()

dir = 'C:\\Users\\king2\\Documents\\Sam Docs\\Python\\Data Apps\\Data Viz Gallery\\'

if option == 'NBA Player Stats':
    df = pd.read_csv(dir + '/Data/NBA_20_21/Player Stats 2020 & 2021.csv')
    df.rename(columns={"'+/-": "+/-"})

    cols = list(df.columns)

    # Choose Input Variables
    x_axis = render_nba_player_stats_options('X-Axis', cols)
    y_axis = render_nba_player_stats_options('Y-Axis', cols)
    size = render_nba_player_stats_options('Size', cols)

    # Create Plot
    fig = plt.figure()
    plt.title(x_axis + 'vs' + y_axis)
    ax = sns.scatterplot(x_axis, y_axis, data=df, size=size)
    plt.legend()
    plt.grid(b=True, which="major", linewidth=0.4)
    st.pyplot(fig)
