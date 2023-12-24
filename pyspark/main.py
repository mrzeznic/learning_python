import pyspark
import pandas as pd
from pyspark import SparkContext

#df = pd.read_csv('data/data.csv')
#print(df)

sc = SparkContext()
n = sc.parallelize([4,10,9,7])
print(n.take(3))
