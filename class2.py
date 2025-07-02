import pandas as pd
import matplotlib.pyplot as plt

df_brazil = pd.read_csv('data/brazilian_imigration_to_canada.csv')

print(df_brazil)
print(df_brazil.info())

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(df_brazil['year'], df_brazil['imigrants'])
ax.set_title('Brazilian Imigration to Canada\n1980-2013')
ax.set_xlabel('Years')
ax.set_ylabel('Number of Imigrants')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
##plt.show()
##------------------------------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(df_brazil['year'], df_brazil['imigrants'], color='blue')
axs[0].set_title('Brazilian Imigration to Canada\n1980-2013')
axs[0].set_xlabel('Years')
axs[0].set_ylabel('Number of Imigrants')
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
axs[0].grid(True)

axs[1].boxplot(df_brazil['imigrants'])
axs[1].set_title('Boxplot of Brazilian Imigration to Canada\n1980-2013')
axs[1].set_xlabel('Brazil')
axs[1].set_ylabel('Number of Imigrants')
axs[1].grid(True)

##plt.show()
##------------------------------------------------------------
df = pd.read_csv('data/canadian_immegration_data.csv')
df.set_index('Country', inplace=True)

years = list(map(str, range(1980, 2014)))

fig, axs = plt.subplots(2,2, figsize=(10,6))
fig.subplots_adjust(hspace=0.5, wspace=0.3)
fig.suptitle('Imigration to Canada by Country\n1980-2013', fontsize=16)

axs[0,0].plot(df.loc['Brazil', years])
axs[0,0].set_title('Brazil')

axs[0,1].plot(df.loc['Colombia', years])
axs[0,1].set_title('Colombia')

axs[1,0].plot(df.loc['Argentina', years])
axs[1,0].set_title('Argentina')

axs[1,1].plot(df.loc['Peru', years])
axs[1,1].set_title('Peru')

for ax in axs.flat:
  ax.xaxis.set_major_locator(plt.MultipleLocator(5))

for ax in axs.flat:
  ax.set_xlabel('Years')
  ax.set_ylabel('Number of Imigrants')

ymin = 0
xmax = 7000

for ax in axs.ravel():
    ax.set_ylim(ymin, xmax)
    ax.grid(True)

plt.show()