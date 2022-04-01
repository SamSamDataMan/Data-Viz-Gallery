import os
import random
from turtle import fillcolor
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, Tooltip
import seaborn as sns
import streamlit as st
from home import render_home
from sidebar import even_bigger_chart, render_option, render_option_nba, render_year_selection, optional_variable_checkbox, render_nba_player_stats_options, bigger_chart

def normalize(values, bounds):
    return [bounds['desired']['lower'] + (x - bounds['actual']['lower']) * (bounds['desired']['upper'] - bounds['desired']['lower']) / (bounds['actual']['upper'] - bounds['actual']['lower']) for x in values]

option = render_option()

base = os.path.dirname(__file__)

if option == 'Home':
    render_home()
elif option == 'NBA':
    df = pd.read_csv(os.path.join(base, 'Data', 'NBA', 'Player Stats.csv'))
    df.rename(columns={"'+/-": "+/-"}, inplace=True)
    cols = list(df.columns)
    option_nba = render_option_nba()
    # if option_nba == 'Year to Year Comparison':
    #     st.title('Hang tight... Page Coming Soon.')
    #     st.title('Player Stats by Season')

    if option_nba == 'Single Season Multi-Stat Comparison':
        st.title('Player Stats by Season')

        year = render_year_selection(df)
        df = df[df['YEAR'] == year]

        # Choose Input Variables
        x_axis = render_nba_player_stats_options('X-Axis', cols, 15)
        y_axis = render_nba_player_stats_options('Y-Axis', cols, 16)
        markersize = optional_variable_checkbox('marker size')

        graph = figure(title=x_axis + ' vs ' + y_axis + ' Over ' + year + ' Season',
                       plot_height=800,
                       plot_width=800,
                       tools=['hover'])

        graph.title.text_font_size = '20pt'
        graph.title.align = 'center'
        graph.title.text_color = '#ffffff'
        graph.xaxis.axis_label = x_axis
        graph.xaxis.axis_label_text_font_size = "16pt"
        graph.xaxis.axis_label_text_color = '#ffffff'
        graph.yaxis.axis_label = y_axis
        graph.yaxis.axis_label_text_font_size = "16pt"
        graph.yaxis.axis_label_text_color = '#ffffff'
        graph.background_fill_color = '#c39c76'
        graph.border_fill_color = '#743e16'

        hover = graph.select(dict(type=HoverTool))

        if markersize:
            size = render_nba_player_stats_options('Size', cols, 0)
            df['markersize'] = (pd.qcut(df[size], 4, labels=False) + 1) * 4
            size_value = 'markersize'
            if size == x_axis or size == y_axis:
                hover.tooltips = [('PLAYER', '@{PLAYER}'), (x_axis, '@' + x_axis + "{0}"), (y_axis, '@' + y_axis + "{0}")]
            else:
                hover.tooltips = [('PLAYER', '@{PLAYER}'), (size, '@' + size + "{0}"), (x_axis, '@' + x_axis + "{0}"), (y_axis, '@' + y_axis + "{0}")]
        else:
            size_value = 9
            hover.tooltips = [('PLAYER', '@{PLAYER}'), (x_axis, '@' + x_axis + "{0}"), (y_axis, '@' + y_axis + "{0}")]

        graph.scatter(x=x_axis,
                      y=y_axis,
                      source=df,
                      size=size_value,
                      fill_color='#f29539',
                      line_color='black',
                      )

        st.bokeh_chart(graph)

        st.write('Data Source: https://www.nba.com/stats')
