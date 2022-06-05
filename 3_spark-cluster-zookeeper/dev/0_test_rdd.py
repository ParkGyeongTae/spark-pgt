from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .appName('0_test_rdd') \
                    .master('spark://spark-master-1:7077,spark-master-2:7077') \
                    .config('spark.driver.cores', '2') \
                    .config('spark.driver.memory','2g') \
                    .config('spark.executor.memory', '2g') \
                    .config('spark.executor.cores', '2') \
                    .config('spark.cores.max', '8') \
                    .getOrCreate()

sc = spark.sparkContext

data_1 = list(range(0, 10))
data_2 = list(range(10, 20))

rdd_1 = sc.parallelize(data_1)
rdd_2 = sc.parallelize(data_2)

rdd_union = rdd_1.union(rdd_2)
rdd_map_type = rdd_union.map(lambda x: type(x))
rdd_map_str = rdd_union.map(lambda x: str(x))
rdd_map_type_2 = rdd_map_str.map(lambda x: type(x))

print()
print(rdd_union)
print(rdd_union.count(), rdd_union.collect())
print()
print(rdd_map_type)
print(rdd_map_type.count(), rdd_map_type.collect())
print()
print(rdd_map_str)
print(rdd_map_str.count(), rdd_map_str.collect())
print()
print(rdd_map_type_2)
print(rdd_map_type_2.count(), rdd_map_type_2.collect())
print()

sc.stop()


'''
from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .appName('0_test_rdd') \
                    .master('spark://spark-master-1:7077,spark-master-2:7077') \
                    .config('spark.driver.cores', '2') \
                    .config('spark.driver.memory','2g') \
                    .config('spark.executor.memory', '2g') \
                    .config('spark.executor.cores', '2') \
                    .config('spark.cores.max', '8') \
                    .getOrCreate()

sc = spark.sparkContext

line_1 = 'i love you'
line_2 = 'you are my friend'
line_3 = 'my name is park'

lines = sc.parallelize([line_1, line_2, line_3])
# lines = sc.parallelize([line_1.upper(), line_2.upper(), line_3.upper()])
# lines = sc.parallelize([line_1.lower(), line_2.lower(), line_3.lower()])

lines_map = lines.map(lambda x: x.split(' '))
lines_flatmap = lines.flatMap(lambda x: x.split(' '))
lines_filter = lines_flatmap.filter(lambda x: len(x) > 3)

print()
print(lines)
print(lines.count(), lines.collect())
print()
print(lines_map)
print(lines_map.count(), lines_map.collect())
print()
print(lines_flatmap)
print(lines_flatmap.count(), lines_flatmap.collect())
print()
print(lines_filter)
print(lines_filter.count(), lines_filter.collect())
print()

sc.stop()
'''



'''
from pyspark.sql import SparkSession

spark = SparkSession\
        .builder\
        .appName("0_save_file")\
        .getOrCreate()

sc = spark.sparkContext

data = sc.parallelize(range(0, 10))
data_map = data.map(lambda x: x * x)

data_reduce = data.reduce(lambda x, y: x + y)
data_map_reduce = data_map.reduce(lambda x, y: x + y)

print(f'data            : {data.collect()}')
print(f'data_map        : {data_map.collect()}')
print(f'data_reduce     : {data_reduce}')
print(f'data_map_reduce : {data_map_reduce}')

spark.stop()
'''


'''
from pyspark.sql import SparkSession

spark = SparkSession\
        .builder\
        .appName("0_save_file")\
        .getOrCreate()

sc = spark.sparkContext

lines = sc.parallelize(['i love you', 'you are my friend', 'my name is park'])

print(f'lines : {lines.collect()}' )

# pairs = lines.map(lambda s: s.split(" ")) # 띄어쓰기로 나누기
# pairs = pairs.filter(lambda x: len(x) > 3) # 단어의 개수가 3개를 초과하는 것만 필터
# pairs = lines.flatMap(lambda x: x.split(" ")).map(lambda word: (word, 1)) # 모든 단어를 map 하기

pairs = lines.flatMap(lambda x: x.split(" ")).map(lambda word: (word, 1)).groupByKey().mapValues(sum).sortByKey(True)

print(f'pairs : {pairs.collect()}' )

spark.stop()
'''

'''
from pyspark.sql import SparkSession

spark = SparkSession\
        .builder\
        .appName("0_save_file")\
        .getOrCreate()

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_rdd = spark.sparkContext.parallelize(alphabet_list)
number_rdd = spark.sparkContext.parallelize(range(0, 26))

# print(alphabet_rdd.collect())
# print(alphabet_rdd.count())
# print(number_rdd.collect())
# print(number_rdd.count())

alphabet_rdd.saveAsTextFile("/home/spark/result/0_save_file")
number_rdd.saveAsTextFile("/home/spark/result/0_save_file")

spark.stop()
'''

'''
from pyspark.sql import SparkSession

spark = SparkSession\
        .builder\
        .appName("0_save_file")\
        .getOrCreate()

sc = spark.sparkContext

line_1 = sc.parallelize(['0', '1', '2', '3', '4'])
line_2 = sc.parallelize(['5', '6', '7', '8', '9'])
line_3 = sc.parallelize(['10', '11', '12', '13', '14'])

line_all = line_1.union(line_2).union(line_3)

line_filter = line_all.filter(lambda x: "1" in x)

print('list_filter 전체 :', f'{line_filter.count()}, {line_filter.collect()}')
print('list_filter 2개 :', f'{line_filter.take(2)}')
print('list_filter 4개 :', f'{line_filter.take(4)}')

spark.stop()
'''