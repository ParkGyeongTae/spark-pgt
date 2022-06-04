from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .appName('3_test_sparksession') \
                    .master('spark://spark-master:17077') \
                    .getOrCreate()

sc = spark.sparkContext

for setting in sc._conf.getAll():
    print(setting)

sc.stop()







# from pyspark.conf import SparkConf
# from pyspark.context import SparkContext

# conf = SparkConf().setAll([('spark.app.name', '2_test_sparkconf'),
#                            ('spark.master', 'spark://spark-master:17077'),
#                            ('spark.driver.cores', '1'),
#                            ('spark.driver.memory','1g'),
#                            ('spark.executor.memory', '1g'),
#                            ('spark.executor.cores', '2'),
#                            ('spark.cores.max', '2')])

# sc = SparkContext(conf = conf)




# sc = spark.sparkConf()
# spark.conf.set('spark.executor.memory', '1g')

# spark.conf.get('spark.executor.memory')
# for i in sc._conf.getAll():
#     print(i)



# conf = SparkConf()

# conf.setMaster('spark://spark-master:17077') \
#     .setAppName('2_test_sparksession') \
#     .set

# sc = SparkContext(conf = conf)
# sqlContext = SQLContext(sc)

# print('spark.master :',   conf.get('spark.master'))
# print('spark.app.name :', conf.get('spark.app.name'))
# print('spark.home :',     conf.get('spark.home'))
# print('spark.home :',     conf.get('spark.driver.memory'))




# print(sc._conf.getAll())


# sc = SparkContext(conf=conf)
# sc.master
# 'local'
# sc.appName
# 'My app'
# sc.sparkHome is None
# True

# from pyspark.conf import SparkConf
# from pyspark.context import SparkContext
# conf = SparkConf()
# conf.setMaster("local").setAppName("My app")
# <pyspark.conf.SparkConf object at ...>
# conf.get("spark.master")



# for i in sc.getConf().getAll():
#     print(i)

# spark.stop()

# from pyspark import SparkConf
# from pyspark import SparkContext
# # from pyspark.sql.functions import lit
# from pyspark.sql.types import DoubleType

# sc.stop()
# conf = SparkConf().setAppName("comstat-test").set("spark.yarn.driver.memoryOverhead", "2048")\
# .set("spark.yarn.executor.memoryOverhead", "2048")\
# .set("spark.default.parallelism", "116")\
# .set("spark.shuffle.compress", "true")\
# .set("spark.io.compression.codec", "snappy")


# from pyspark.conf import SparkConf
# from pyspark.context import SparkContext
# from pyspark.sql import SQLContext, SparkSession

# spark = SparkSession.builder \
#                     .appName('2_test_sparksession') \
#                     .master('spark://spark-master:17077') \
#                     .getOrCreate()

# conf = SparkConf()

# conf.setMaster('spark://spark-master:17077') \
#     .setAppName('2_test_sparksession') \
#     .set

# sc = SparkContext(conf = conf)
# sqlContext = SQLContext(sc)

# # print('spark.master :',   conf.get('spark.master'))
# # print('spark.app.name :', conf.get('spark.app.name'))
# # print('spark.home :',     conf.get('spark.home'))
# # print('spark.home :',     conf.get('spark.driver.memory'))




# # print(sc._conf.getAll())

# for i in sc._conf.getAll():
#     print(i)

# sc.stop()