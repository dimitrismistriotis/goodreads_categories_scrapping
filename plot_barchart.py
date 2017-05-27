import math as math
import matplotlib.pyplot as plt
import pandas as pd

data = pd.Series({'cat1': 8200000, 'cat2': 6800123, 'cat3': 7800000, 'cat4': 6000000,
                 'cat5': 4300000, 'cat6': 4100000, 'cat7': 3800000, 'cat8': 3500000,
                 'cat9': 3400000, 'cat10': 3300000})

# data.plot(kind='barh', color='k')
# Very nice up to here, but not what I want...

dataf = pd.DataFrame(data, columns=['books_published'])

max_value = dataf.max()['books_published']
annotation_divisior = 10 ** (math.floor(math.log(max_value, 10)))

dataf['color'] = '#afafaf'
dataf.loc[dataf['books_published'] == max_value, ['color']] = '#f70e0e'
#dataf.loc[dataf['books_published'] != max_value, ['color']] = '#afafaf'

dataf = dataf.sort_values(['books_published'], ascending=[True])

#
# Stack Overflow to the rescue for annotating(!):
# http://stackoverflow.com/questions/23591254/python-pandas-matplotlib-annotating-labels-above-bar-chart-columns

ax = dataf.plot(kind='barh', legend=False,
                  color=[dataf['color']],
                  linestyle=None,
                  # title="Books published per category",
                  figsize=(15, 10), fontsize=20)

for p in ax.patches:
    ax.annotate("%.1f" % (p.get_width() / annotation_divisior),
                (p.get_x() + p.get_width(), p.get_y()), xytext=(5, 10),
                textcoords='offset points', fontsize=18)

fig = ax.get_figure()
fig.savefig('diagram.png')
