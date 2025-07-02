import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

top_10 = pd.read_csv('data/canadian_immegration_data.csv')
top_10 = top_10.sort_values(by='Total', ascending=False).head(10)
top_10.set_index('Country', inplace=True)

def generate_chart_pallete(palette):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax = sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h', palette=palette)
    ax.set_title('Countries with more imigrants to Canada\n1980 a 2013', loc='left', fontsize=16)
    ax.set_xlabel('Number of Imigrants', fontsize=14)
    ax.set_ylabel('', fontsize=14)
    plt.show()

generate_chart_pallete('rocket')
generate_chart_pallete('blues_r')

sns.set_theme(style='dark')
generate_chart_pallete("tab10")