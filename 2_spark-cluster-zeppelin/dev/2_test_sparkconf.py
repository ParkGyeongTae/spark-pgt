
from pyspark.conf import SparkConf
from pyspark.context import SparkContext

conf = SparkConf().setAll([('spark.app.name', '2_test_sparkconf'),
                           ('spark.master', 'spark://spark-master:17077'),
                           ('spark.driver.cores', '1'),
                           ('spark.driver.memory','1g'),
                           ('spark.executor.memory', '1g'),
                           ('spark.executor.cores', '2'),
                           ('spark.cores.max', '2')])

sc = SparkContext(conf = conf)

for setting in sc._conf.getAll():
    print(setting)

sc.stop()


'''
from pyspark.conf import SparkConf
from pyspark.context import SparkContext

conf = SparkConf().setAll([('spark.app.name', '2_test_sparkconf'),
                           ('spark.master', 'spark://spark-master:17077'),
                           ('spark.driver.cores', '1'),
                           ('spark.driver.memory','1g'),
                           ('spark.executor.memory', '1g'),
                           ('spark.executor.cores', '2'),
                           ('spark.cores.max', '2')])

sc = SparkContext(conf = conf)

for setting in sc._conf.getAll():
    print(setting)

sc.stop()
'''

'''
from pyspark.conf import SparkConf
from pyspark.context import SparkContext

conf = SparkConf().setAll([('spark.app.name', '2_test_sparkconf'),
                           ('spark.master', 'spark://spark-master:17077')])
sc = SparkContext(conf = conf)

print('first')
for setting in sc._conf.getAll():
    print(setting)

sc.stop()

conf = SparkConf().setAll([('spark.app.name', '2_test_sparkconf'),
                           ('spark.master', 'spark://spark-master:17077'),
                           ('spark.driver.cores', '1'),
                           ('spark.driver.memory','1g'),
                           ('spark.executor.memory', '1g'),
                           ('spark.executor.cores', '2'),
                           ('spark.cores.max', '2')])

sc = SparkContext(conf = conf)

print('second')
for setting in sc._conf.getAll():
    print(setting)

sc.stop()
'''