from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark import SparkContext

spark = SparkSession \
        .builder \
        .appName("2_test_sparksession") \
        .master('spark://spark-master:17077') \
        .getOrCreate()

sc = spark.sparkContext

print(SparkConf())
exit()

for i in sc.getConf().getAll():
    print(i)

spark.stop()

from pyspark import SparkConf
from pyspark import SparkContext
# from pyspark.sql.functions import lit
# from pyspark.sql.types import DoubleType

# sc.stop()
# conf = SparkConf().setAppName("comstat-test").set("spark.yarn.driver.memoryOverhead", "2048")\
# .set("spark.yarn.executor.memoryOverhead", "2048")\
# .set("spark.default.parallelism", "116")\
# .set("spark.shuffle.compress", "true")\
# .set("spark.io.compression.codec", "snappy")
