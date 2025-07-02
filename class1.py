import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/canadian_immegration_data.csv')

print(df)
print(df.info())

df.set_index('Country', inplace=True)

years = list(map(str, range(1980, 2014)))
brazil = df.loc['Brazil', years]

brazil_dict = {
    'year': brazil.index.tolist(), 
    'imigrants': brazil.values.tolist()
}

data_brazil = pd.DataFrame(brazil_dict)

print(data_brazil)

plt.figure(figsize=(8,4))
plt.plot(data_brazil['year'], data_brazil['imigrants'])
plt.title('Brazilian Imigration to Canada (1980-2013)')
plt.xlabel('Years')
plt.ylabel('Number of Imigrants')
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
plt.show()