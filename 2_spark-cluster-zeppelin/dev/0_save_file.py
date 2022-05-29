from pyspark.sql import SparkSession

if __name__ == "__main__":

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
