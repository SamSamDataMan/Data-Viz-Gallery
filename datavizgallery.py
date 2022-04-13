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
from sidebar import render_option, render_option_nba, render_year_selection, optional_variable_checkbox, render_nba_player_stats_options, season_slider

def normalize(values, bounds):
    return [bounds['desired']['lower'] + (x - bounds['actual']['lower']) * (bounds['desired']['upper'] - bounds['desired']['lower']) / (bounds['actual']['upper'] - bounds['actual']['lower']) for x in values]

option = render_option()

base = os.path.dirname(__file__)

if option == 'Home':
    render_home()
elif option == 'NBA':
    df = pd.read_csv(os.path.join(base, 'Data', 'NBA', 'Player Stats.csv'))
    cols = list(df.columns)
    option_nba = render_option_nba()

    df = (df
          [cols]
          .assign(
                # Per Game Stats
                MIN_PG=round((df.MIN / df.GP), 2),
                PTS_PG=round((df.PTS / df.GP), 2),
                FGM_PG=round((df.FGM / df.GP), 2),
                FGA_PG=round((df.FGA / df.GP), 2),
                TPM_PG=round((df['3PM'] / df.GP), 2),
                TPA_PG=round((df['3PA'] / df.GP), 2),
                FTM_PG=round((df.FTM / df.GP), 2),
                FTA_PG=round((df.FTA / df.GP), 2),
                OREB_PG=round((df.OREB / df.GP), 2),
                DREB_PG=round((df.DREB / df.GP), 2),
                REB_PG=round((df.REB / df.GP), 2),
                AST_PG=round((df.AST / df.GP), 2),
                TOV_PG=round((df.TOV / df.GP), 2),
                STL_PG=round((df.STL / df.GP), 2),
                BLK_PG=round((df.BLK / df.GP), 2),
                PF_PG=round((df.PF / df.GP), 2),
                FP_PG=round((df.FP / df.GP), 2),
                Plus_Minus_PG=round((df['+/-'] / df.GP), 2),
                # Per 36 Minute Stats(df.MIN/36)
                PTS_Per36=round((df.PTS / (df.MIN / 36)), 2),
                FGM_Per36=round((df.FGM / (df.MIN / 36)), 2),
                FGA_Per36=round((df.FGA / (df.MIN / 36)), 2),
                TPM_Per36=round((df['3PM'] / (df.MIN / 36)), 2),
                TPA_Per36=round((df['3PA'] / (df.MIN / 36)), 2),
                FTM_Per36=round((df.FTM / (df.MIN / 36)), 2),
                FTA_Per36=round((df.FTA / (df.MIN / 36)), 2),
                OREB_Per36=round((df.OREB / (df.MIN / 36)), 2),
                DREB_Per36=round((df.DREB / (df.MIN / 36)), 2),
                REB_Per36=round((df.REB / (df.MIN / 36)), 2),
                AST_Per36=round((df.AST / (df.MIN / 36)), 2),
                TOV_Per36=round((df.TOV / (df.MIN / 36)), 2),
                STL_Per36=round((df.STL / (df.MIN / 36)), 2),
                BLK_Per36=round((df.BLK / (df.MIN / 36)), 2),
                PF_Per36=round((df.PF / (df.MIN / 36)), 2),
                FP_Per36=round((df.FP / (df.MIN / 36)), 2),
                Plus_Minus_Per36=round((df['+/-'] / (df.MIN / 36)), 2),
                )
          .rename(columns={
                        'TPM_PG': '3PM_PG',
                        'TPA_PG': '3PA_PG',
                        'TPM_Per36': '3PM_Per36',
                        'TPA_Per36': '3PA_Per36',
                        '+/-': 'Plus_Minus'
                        #'PlusMinus_PG': '+/-_PG',
                        #'PlusMinus_Per36': '+/-_Per36',
                        }
                  )
          )

    cols = list(df.columns)
  
    if option_nba == 'Player Stats Over Time':
        years = list(df.BEGIN_YEAR.unique())
        year_low, year_high = season_slider(years)
        st.text(year_low)
        st.text(year_high)
        st.title('Hang tight... Page Coming Soon.')
        st.title('Player Stats by Season')
        df_1 = df[df['BEGIN_YEAR'] == year_low]
        df_2 = df[df['BEGIN_YEAR'] == year_high]
        st.text(df_1.head())
        st.text(df_2.head())
        stat = 'MIN'
        df_merged = df_1[['PLAYER', stat]].merge(df_2[['PLAYER', stat]], how='inner', on='PLAYER')
        st.text(df_merged.head())

    if option_nba == 'Player Stats by Season':
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
                hover.tooltips = [('PLAYER', '@{PLAYER}'), (x_axis, '@' + x_axis + "{0.0}"), (y_axis, '@' + y_axis + "{0.0}")]
            else:
                hover.tooltips = [('PLAYER', '@{PLAYER}'), (size, '@' + size + "{0.0}"), (x_axis, '@' + x_axis + "{0.0}"), (y_axis, '@' + y_axis + "{0.0}")]
        else:
            size_value = 9
            hover.tooltips = [('PLAYER', '@{PLAYER}'), (x_axis, '@' + x_axis + "{0.0}"), (y_axis, '@' + y_axis + "{0.0}")]

        graph.scatter(x=x_axis,
                      y=y_axis,
                      source=df,
                      size=size_value,
                      fill_color='#f29539',
                      line_color='black',
                      )

        st.bokeh_chart(graph)

        st.write('Data Source: https://www.nba.com/stats')
