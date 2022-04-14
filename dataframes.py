import pandas as pd
import os

def nba_player_stats():
    base = os.path.dirname(__file__)
    df = pd.read_csv(os.path.join(base, 'Data', 'NBA', 'Player Stats.csv'))
    cols = list(df.columns)

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
              # 'PlusMinus_PG': '+/-_PG',
              # 'PlusMinus_Per36': '+/-_Per36',
              }
            )
        )

    return df
