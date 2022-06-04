from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .appName('3_test_sparksession') \
                    .master('spark://spark-master:17077') \
                    .config('spark.driver.cores', '1') \
                    .config('spark.driver.memory','1g') \
                    .config('spark.executor.memory', '2g') \
                    .config('spark.executor.cores', '2') \
                    .config('spark.cores.max', '8') \
                    .getOrCreate()

sc = spark.sparkContext

data = sc.parallelize(range(0, 10000000))
# print(data.collect())


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

'''
from pyspark.sql import SparkSession
import time

start_time = time.time()

spark = SparkSession.builder \
                    .appName('3_test_sparksession') \
                    .master('spark://spark-master:17077') \
                    .config('spark.driver.cores', '1') \
                    .config('spark.driver.memory','1g') \
                    .config('spark.executor.memory', '2g') \
                    .config('spark.executor.cores', '2') \
                    .config('spark.cores.max', '2') \
                    .getOrCreate()

created_time = time.time()

sc = spark.sparkContext

data = sc.parallelize(range(0, 10000000))
data.collect()

end_time = time.time()

print(round(end_time - created_time, 2))
print(round(end_time - start_time, 2))
print(round(created_time - start_time, 2))

sc.stop()
'''