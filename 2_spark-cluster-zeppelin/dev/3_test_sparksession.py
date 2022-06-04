from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .appName('3_test_sparksession') \
                    .master('spark://spark-master:17077') \
                    .getOrCreate()

sc = spark.sparkContext

for setting in sc._conf.getAll():
    print(setting)

sc.stop()

'''
from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .appName('3_test_sparksession') \
                    .master('spark://spark-master:17077') \
                    .getOrCreate()

sc = spark.sparkContext

for setting in sc._conf.getAll():
    print(setting)

sc.stop()
'''