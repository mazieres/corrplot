import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
from matplotlib.patches import Circle
from scipy.stats import pearsonr
from itertools import combinations

def myCorrPlot(df):
	"""
	Correlation plot ( ~ corrplot with R)

	Takes a Pandas DataFrame as input and returns
	the plot which can then be shown with
    plot.show(), saved to a file with plot.savefig(), or
    manipulated in any other standard matplotlib way.

	Forked from https://github.com/louridas/corrplot
	"""
	plt.figure(1)
	ax = plt.subplot(1, 1, 1, aspect='equal')
	poscm = cm.get_cmap('Blues')
	negcm = cm.get_cmap('Reds')
	labels = df.columns

	for pair in combinations(labels, 2):
		corr = pearsonr(df[pair[0]].values, df[pair[1]].values)[0]
		clrmap = poscm if corr >= 0 else negcm
		circle = Circle((labels.get_loc(pair[0]),labels.get_loc(pair[1])), radius = 0.4)
		circle.set_edgecolor('black')
		circle.set_facecolor(clrmap(np.abs(corr)))
		mirrorCircle = Circle((labels.get_loc(pair[1]),labels.get_loc(pair[0])), radius = 0.4)
		mirrorCircle.set_edgecolor('black')
		mirrorCircle.set_facecolor(clrmap(np.abs(corr)))
		ax.add_artist(circle)
		ax.add_artist(mirrorCircle)

	ax.set_xlim(-1, len(labels))
	ax.set_ylim(-1, len(labels))
		
	ax.xaxis.tick_top()
	xtickslocs = np.arange(len(labels))
	ax.set_xticks(xtickslocs)
	ax.set_xticklabels(labels, rotation=30, fontsize='small', ha='left')

	ax.invert_yaxis()
	ytickslocs = np.arange(len(labels))
	ax.set_yticks(ytickslocs)
	ax.set_yticklabels(labels, fontsize='small')
	
	return plt

if __name__ == '__main__':
	pass
	# # An example with the IRIS dataset
	# from sklearn import datasets
	# iris = datasets.load_iris()
	# df = pd.DataFrame(iris.data, columns=iris.feature_names)
	# plot = myCorrPlot(df)
	# plot.show()