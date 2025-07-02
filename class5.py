import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df_brazil = pd.read_csv('data/brazilian_imigration_to_canada.csv')

fig = px.line(
    df_brazil, 
    x='year', 
    y='imigrants',
    title='Brazilian Imigration to Canada (1980-2013)',
    labels={'year': 'Years', 'imigrant': 'Number of Imigrants'}
)
fig.update_traces(
    line=dict(color='blue', width=3),
    marker=dict(symbol='circle', size=6)
)
fig.update_layout(
    width=1000, 
    height=500,
    font_family='Arial',
    font_size=14,
    font_color='grey',
    title_font_color='black',
    title_font_size=16,
    xaxis={
        'tickangle': -45
    },
    xaxis_title='Years',
    yaxis_title='Number of Imigrants'
)
fig.show()
fig.write_html('imgs/imigration_brazil_to_canada.html')

df = pd.read_csv('data/canadian_immegration_data.csv')
south_america = df.query("Region == 'South America'")
south_america.set_index('Country', inplace=True)
south_america.drop(['Continent', 'Region', 'Total'], axis=1, inplace=True)
south_america_clean = south_america.T

fig = px.line(
    south_america_clean, 
    x=south_america_clean.index, 
    y=south_america_clean.columns,
    color='Country',
    markers=True,
    title='South America Imigration to Canada (1980-2013)',
    labels={'value': 'Number of Imigrants', 'variable': 'Country'}
)
fig.update_layout(
    width=1000, 
    height=500,
    font_family='Arial',
    font_size=14,
    font_color='grey',
    title_font_color='black',
    title_font_size=16,
    xaxis_title='Years',
    yaxis_title='Number of Imigrants',
    xaxis={
        'tickangle': -45
    }
)
fig.show()
fig.write_html('imgs/imigration_south_america_to_canada.html')