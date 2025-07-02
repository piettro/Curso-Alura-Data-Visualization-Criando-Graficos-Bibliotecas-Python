import pandas as pd
import matplotlib.pyplot as plt

df_brazil = pd.read_csv('data/brazilian_imigration_to_canada.csv')

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(df_brazil['year'], df_brazil['imigrants'], color='blue', marker='o', linestyle='-',lw=3)
ax.set_title('Brazilian Imigration to Canada\n1980-2013', fontsize=16, loc='left')
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Number of Imigrants', fontsize=14)
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.savefig('imgs/brazil_imigration_to_canada.png', transparent=False, dpi=300, bbox_inches='tight')

plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

##------------------------------------------------------------
df = pd.read_csv('data/canadian_immegration_data.csv')
south_america = df.query("Region == 'South America'")
south_america_sorted = south_america.sort_values(by='Total', ascending=True)

colors = []
for country in south_america_sorted['Country']:
    if country == 'Brazil':
        colors.append('green')
    else:
        colors.append('silver')

fig, ax = plt.subplots(figsize=(15, 5))
ax.barh(south_america_sorted['Country'], south_america_sorted['Total'], color=colors)
ax.set_title('South America Imigration to Canada\n1980-2013', loc='left', fontsize=18)
ax.set_xlabel('Number of Imigrants', fontsize=14)
ax.set_ylabel('')
ax.yaxis.set_tick_params(labelsize=12)
ax.xaxis.set_tick_params(labelsize=12)

for i, v in enumerate(south_america_sorted['Total']):
    ax.text(v + 20, i, str(format(v,",")), color='black', fontsize=10, ha='left', va='center')

ax.set_frame_on(False)
ax.get_xaxis().set_visible(False)
ax.tick_params(axis='both', which='both', length=0)

fig.savefig('imgs/south_america_imigration_to_canada.png', transparent=False, dpi=300, bbox_inches='tight')
plt.show()
