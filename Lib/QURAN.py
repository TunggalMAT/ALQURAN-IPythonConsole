# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 08:17:43 2019

@author: tunggalmat
"""

import pandas as pd
pd.options.display.max_colwidth = 10000

from csv import QUOTE_NONE
def read_and_reformat(csv_path, encoding='utf-8'):
    df = pd.read_csv(csv_path,
                     sep='|',
                     encoding=encoding,
                     dtype=object,
                     header=None,
                     quoting=QUOTE_NONE,
                     names=['Surah', 'Ayah', 'Text'])    
    df['Text'] = df['Text'].str.replace('#NAME\?', '')
    df['Text'] = df['Text'].str.strip(',')
    return df

indo = read_and_reformat('Dataset/Indonesian.csv')
arab = read_and_reformat('Dataset/Arabic-Original.csv')

arab = arab.rename(columns={'Text':'Arab'})
indo = indo.rename(columns={'Text':'Terjemahan'})

df = pd.merge(arab, indo, how='outer')

#Make Columns Juz
for col in ['Surah', 'Ayah']:
    df[col] = pd.to_numeric(df[col])

def idx(i, j):
    df['index'] = df.index
    return int(df.loc[(df['Surah']==i) & (df['Ayah']==j), 'index'])

cut_points = [-1, idx(2,141), idx(2,252), idx(3,92), idx(4,23), idx(4,147), idx(5,81), idx(6,110), idx(7,87), idx(8,40),
             idx(9,92), idx(11,5), idx(12,52), idx(14,52), idx(16,128), idx(18,74), idx(20,135), idx(22,78), idx(25,20),
             idx(27,55), idx(29,45), idx(33,30), idx(36,27), idx(39,31), idx(41,46), idx(45,37), idx(51,30), idx(57,29),
             idx(66,12), idx(77,50), idx(114,6)]
label_names = [str(i) for i in range(1, len(cut_points))]

if 'Juz' not in df.columns:
    df.insert(2, 'Juz', pd.cut(df.index,cut_points,labels=label_names))
df.drop('index', axis=1, inplace=True)
df['Juz'] = pd.to_numeric(df['Juz'])

#Backup Dataframe
df_backup = df.copy()

class cari:
    def __init__(self):
        self = self
        
    def SurahAyah(self,S,A):
        x = df.loc[(df['Surah'] == S) & (df['Ayah'] == A)]
        return x

    def Surah(self,S):
        x = df.loc[(df['Surah'] == S)]
        return x

    def Ayah(self,A):
        x = df.loc[(df['Ayah'] == A)]
        return x

    def Juz(self,J):
        x = df.loc[(df['Juz'] == J)]
        return x
    
    def Word(self,W):
        df['Terjemahan'] = df['Terjemahan'].str.lower()
        z = df[df['Terjemahan'].str.contains(W.lower())]
        data=[]
        for i in range(z.shape[0]):
            y = df_backup[(df_backup['Surah']==int(z.Surah.values[i])) & (df_backup['Ayah']==int(z.Ayah.values[i]))]
            data.append(y.values[0])
        x = pd.DataFrame(data,columns=['Surah','Ayah','Juz','Arab','Terjemahan'])
        return x
    
    def show(self,z):
        for i in range(z.shape[0]):
            print('\nSurah : ',z.Surah.values[i])
            print('Ayah  : ',z.Ayah.values[i])
            print('Juz   : ',z.Juz.values[i])
            print('Arab  :\n',z.Arab.values[i])
            print('Indonesian :\n ',z.Terjemahan.values[i])
            print('\n----------------------------------------------------------\n')
        input("Press Enter to continue...")