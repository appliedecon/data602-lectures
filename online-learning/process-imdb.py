import tarfile

with tarfile.open('data/aclImdb_v1.tar.gz', 'r:gz') as tar:
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tar)

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