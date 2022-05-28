import sys
from random import random
from operator import add
from time import sleep

from pyspark.sql import SparkSession


if __name__ == "__main__":

    spark = SparkSession\
            .builder\
            .appName("0_save_file")\
            .getOrCreate()
    
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    spark_rdd = spark.sparkContext.parallelize(alphabet_list).collect()

    for i in spark_rdd:
        print(i)
        sleep(1)

    # print(spark_rdd)
    
    # print(alphabet_list)

    # partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    # n = 100000 * partitions

    # def f(_):
    #     x = random() * 2 - 1
    #     y = random() * 2 - 1
    #     return 1 if x ** 2 + y ** 2 <= 1 else 0

    # count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    # print("Pi is roughly %f" % (4.0 * count / n))

    spark.stop()