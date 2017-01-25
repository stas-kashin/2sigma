import pandas as pd

# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_hdf("input/train.h5")

# print df.shape
#
# print df.head()

df_clean = df.dropna(axis='index', how='any')
print df_clean.shape
