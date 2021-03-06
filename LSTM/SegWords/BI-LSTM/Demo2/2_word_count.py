# -*- coding: utf-8 -*-
import sys
import pandas as pd
import numpy as np

"""
注：最终未使用该方法，计算性能不好
"""
import datetime

starttime = datetime.datetime.now()
print("开始时间：" + str(starttime))

# corpusAll = "/Users/sunlu/Workspaces/PyCharm/Github/NLPLearnNote/LSTM/SegWords/BI-LSTM/Demo2/Corpora/people2014All.txt"
corpusAll = sys.argv[1]

inp = open(corpusAll, 'r')
lines = ""
for line in inp:
    lines = lines + line
inp.close()

str = []
for i in lines:
    str = str + [i]

df1 = pd.DataFrame({"col1": str})
df1['col2'] = 1
df2 = df1.groupby('col1').agg(sum)
df3 = df2[df2.col2 >= 3]
df3['col3'] = df3.index.tolist()
df3 = df3[['col3','col2']]

# outputFile = "/Users/sunlu/Workspaces/PyCharm/Github/NLPLearnNote/LSTM/SegWords/BI-LSTM/Demo2/results/pre_vocab.txt"
outputFile = sys.argv[2]
df3.to_csv(outputFile,
           encoding = 'utf-8', index=False,header=False)

endtime = datetime.datetime.now()
print("结束时间：" + str(endtime))

print("word count运行时间：" + str((endtime - starttime).days))