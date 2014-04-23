# CorrPlot


Create a correlation plot, as in the corrplot R package.

This is a simplified fork of <https://github.com/louridas/corrplot>

It takes a Pandas.DataFrame as input and returns a plot.

# Example

```python
from sklearn import datasets
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
```

(https://raw.githubusercontent.com/mazieres/corrplot/master/exampleIRIS.png "CorrPlot on IRIS")