
'''
from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession\
        .builder\
        .appName("0_save_file")\
        .getOrCreate()

sc = spark.sparkContext

data_1 = [("kim", 1), ("park", 2), ("choi", 3)]

data_2 = [Row(name='kim',  age=5,  height=80),
        Row(name='park', age=5,  height=80),
        Row(name='choi', age=10, height=80)]

df_1 = sc.parallelize(data_1).toDF()
df_2 = sc.parallelize(data_2).toDF()

print(df_1.show())
print(df_2.show())

spark.stop()
'''

'''
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession \
        .builder \
        .appName("1_test_dataframe") \
        .getOrCreate()

schema = StructType([StructField("first",  StringType(), True),
                     StructField("second", StringType(), True),
                     StructField("third",  StringType(), True)])

df = spark.read.csv('/home/spark/result/1_test_dataframe.csv', header = False, schema = schema)

df.show()
spark.stop()
'''

from pyspark.sql import SparkSession
import numpy as np
import pandas as pd

spark = SparkSession \
        .builder \
        .appName('1_test_dataframe') \
        .getOrCreate()

df_pandas = pd.DataFrame(np.random.rand(100, 3))
df_pandas.columns = ['first', 'second', 'third']

df_spark = spark.createDataFrame(df_pandas)
df_re_pandas = df_spark.select('*').toPandas()

print(df_pandas.head(5))
print(df_spark.show(5))
print(df_re_pandas.head(5))

spark.stop()