from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("2_test_sparksession") \
        .master('spark://spark-master:17077') \
        .getOrCreate()

sc = spark.sparkContext

print(sc.getConf().getAll())

spark.stop()