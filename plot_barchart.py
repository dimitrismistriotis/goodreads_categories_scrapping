import math as math
import matplotlib.pyplot as plt
import pandas as pd

dataf = pd.read_csv('cagetories_books.csv')
dataf.columns = ['Category', 'Books']

# max_value = dataf.max()['books_published']
max_value = dataf.max()['Books'] # first column... works
annotation_divisior = 10 ** (math.floor(math.log(max_value, 10)))

dataf['color'] = '#afafaf'
dataf.loc[dataf['Books'] == max_value, ['color']] = '#f70e0e'
#dataf.loc[dataf['books_published'] != max_value, ['color']] = '#afafaf'

dataf = dataf.sort_values(['Books'], ascending=[True])

top_ten = dataf[-10:]
#
# Stack Overflow to the rescue for annotating(!):
# http://stackoverflow.com/questions/23591254/python-pandas-matplotlib-annotating-labels-above-bar-chart-columns
#

ax = top_ten.plot(kind='barh', legend=False,
                  color=[top_ten['color']],
                  linestyle=None,
                  x='Category',
                  # title="Books published per category",
                  figsize=(25, 10), fontsize=20)

for p in ax.patches:
    ax.annotate("%.1f" % (p.get_width() / annotation_divisior),
                (p.get_x() + p.get_width(), p.get_y()), xytext=(5, 10),
                textcoords='offset points', fontsize=18)

fig = ax.get_figure()
fig.savefig('diagram.png')
