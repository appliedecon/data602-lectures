import tarfile

with tarfile.open('data/aclImdb_v1.tar.gz', 'r:gz') as tar:
    tar.extractall()

import pyprind
import pandas as pd
import os

basepath = 'aclImdb'

labels = {'pos':1, 'neg':0}
pbar = pyprind.ProgBar(50000)

df = pd.DataFrame()

for s in ('test','train'):
    for l in ('pos','neg'):
        path = os.path.join(basepath, s, l)
        for file in sorted(os.listdir(path)):
            with open(os.path.join(path, file), 'r', encoding='utf-8') as infile:
                txt = infile.read()
            df = df.append([[txt, labels[l]]], ignore_index=True)
            pbar.update()

df.columns = ['review', 'sentiment']
df.head()

import numpy as np

np.random.seed(0)

df = df.reindex(np.random.permutation(df.index))
df.head()

df.to_csv('data/imdb.csv', index=False, encoding='utf-8')
df = pd.read_csv('data/imdb.csv', encoding='utf-8')
df.head()