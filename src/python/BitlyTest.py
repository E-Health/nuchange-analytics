__author__ = 'beapen'


import json
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
#import pandas as pd

path = '../../res/personal/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

frame = DataFrame(records)
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz ==''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])
myplot = tz_counts[:10].plot(kind='barh', rot=0)

plt.savefig('../../target/BitlyTest.png')

