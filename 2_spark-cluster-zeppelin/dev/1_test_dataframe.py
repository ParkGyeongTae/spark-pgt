from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder \
                    .appName("1_test_dataframe") \
                    .master('spark://spark-master:17077') \
                    .getOrCreate()

sc = spark.sparkContext

data = [Row(id = 0, name = 'a', age = 12, type = 'A', score = 90, year = 2012),
        Row(id = 1, name = 'a', age = 15, type = 'B', score = 80, year = 2013),
        Row(id = 2, name = 'b', age = 15, type = 'B', score = 80, year = 2014),
        Row(id = 3, name = 'b', age = 21, type = 'F', score = 50, year = 2015),
        Row(id = 4, name = 'c', age = 15, type = 'C', score = 70, year = 2016),
        Row(id = 5, name = 'c', age = 33, type = 'F', score = 50, year = 2017)]

spark_df = sc.parallelize(data).toDF()

spark_df.createOrReplaceTempView("my_table")
# spark_df.createGlobalTempView("my_table")

spark_sql = spark.sql("SELECT * FROM my_table")
# spark_sql = spark.sql("SELECT * FROM global_temp.my_table")

spark_sql.show()

spark.stop()

# spark_df = spark_df.sql('SELECT * FROM spark_df')

# spark_df = spark_df.select('*')
# spark_df = spark_df.select('name', 'age', 'year')
# spark_df = spark_df.filter(spark_df.age > 20).filter(spark_df.year > 2016)
# spark_df = spark_df.groupBy('name').sum('score').select('*')
# spark_df = spark_df.groupBy('name').agg(sum('age').alias('sum_age'), 
#                                         sum('score').alias('sum_age'), 
#                                         sum('year').alias('sum_year')).select('*')

# spark_df.show()




'''
from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession\
        .builder\
        .appName("1_test_dataframe")\
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
'''

'''
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import max, avg, sum, min

spark = SparkSession.builder \
                    .appName("1_test_dataframe") \
                    .master('spark://spark-master:17077') \
                    .getOrCreate()

sc = spark.sparkContext

data = [Row(name = 'a', age = 12, type = 'A', score = 90, year = 2012),
        Row(name = 'a', age = 15, type = 'B', score = 80, year = 2013),
        Row(name = 'b', age = 15, type = 'B', score = 80, year = 2014),
        Row(name = 'b', age = 21, type = 'F', score = 50, year = 2015),
        Row(name = 'c', age = 15, type = 'C', score = 70, year = 2016),
        Row(name = 'c', age = 33, type = 'F', score = 50, year = 2017)]

spark_df = sc.parallelize(data).sql()

spark_df = spark_df.sql('SELECT * FROM spark_df')

# spark_df = spark_df.select('*')
# spark_df = spark_df.select('name', 'age', 'year')
# spark_df = spark_df.filter(spark_df.age > 20).filter(spark_df.year > 2016)
# spark_df = spark_df.groupBy('name').sum('score').select('*')
# spark_df = spark_df.groupBy('name').agg(sum('age').alias('sum_age'), 
#                                         sum('score').alias('sum_age'), 
#                                         sum('year').alias('sum_year')).select('*')

spark_df.show()

spark.stop()
'''