import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',12)

wcwomen_df = pd.read_csv('matches_1991_2023.csv')
wcmen_df   = pd.read_csv('matches_1930_2022.csv')
wc = pd.concat((wcwomen_df,wcmen_df)).reset_index()

nomes_traduzidos = {'home_team': 'time_1', 'away_team': 'time_2', 'home_score': 'gols_1', 'away_score': 'gols_2',
                    'Date': 'data', 'Year': 'ano', 'Host': 'país_sede', 'Attendance': 'comparecimento',
                    'Score': 'resultado', 'Round': 'rodada', 'home_goal': 'gols_1_detalhes', 'away_goal': 'gols_2_detalhes',
                    'home_own_goal': 'gols_1_contra', 'away_own_goal': 'gols_2_contra',
                    'home_penalty_goal': 'gols_1_penalti', 'away_penalty_goal': 'gols_2_penalti',
                    'home_red_card': 'cartao_vermelho_1', 'away_red_card': 'cartao_vermelho_2',
                    'home_yellow_card_long': 'cartao_amarelo_1', 'away_yellow_card_long': 'cartao_amarelo_2'}

wc = wc.loc[:, nomes_traduzidos.keys()]
wc.columns = nomes_traduzidos.values()

copa = wc['ano'].apply( lambda x: 'Masculina' if x % 2 == 0 else 'Feminina').astype('string')
wc['copa'] = copa
print(wc)