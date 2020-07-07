import numpy as np # linear algebra
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
# matplotlib inline
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

# sns.set_style("darkgrid", {"axes.facecolor": ".95"})
sns.set()
y = pd.read_csv("tsne_senti2.csv",encoding='utf-8')
X = pd.read_csv("features_for_Rumor Data.csv_.csv",encoding='utf-8')
# print(y.head(10))

pca = PCA(0.95)
X_pca = pca.fit_transform(X)
tsne = TSNE(random_state=0)
X_tsne = tsne.fit_transform(X_pca) 


tsne_df = pd.DataFrame(X_tsne)
tsne_df.columns = ["X", "Y"]
tsne_df["labels"] = y
# print(tsne_df.head(10))
ax = sns.scatterplot(x="X", y="Y",hue="labels", data=tsne_df)


# matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
# proj = pd.DataFrame(X_tsne)
# proj.columns = ["comp_1", "comp_2"]
# proj["labels"] = y
# sns.lmplot("comp_1", "comp_2", hue = "labels", data = proj ,fit_reg=False)

plt.show()