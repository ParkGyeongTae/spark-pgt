# 실행 예시

## spark-shell

### scala (spark-shell)

1. (default) ./spark/bin/spark-shell --master spark://spark-master:17077 --name spark-shell-pgt --deploy-mode client --driver-memory 1g
2. (default) ./spark/bin/spark-shell --master spark://spark-master:17077 --name spark-shell-pgt --deploy-mode client --driver-memory 1g
3. (default) ./spark/bin/spark-shell --master spark://spark-master:17077 --name spark-shell-pgt --executor-cores 4 --executor-memory 1g
4. (2c, 1g) ./spark/bin/spark-shell --master spark://spark-master:17077 --name spark-shell-pgt --executor-cores 2 --executor-memory 1g
5. (1c, 1g) ./spark/bin/spark-shell --master spark://spark-master:17077 --name spark-shell-pgt --executor-cores 1 --executor-memory 1g --total-executor-cores 2

### python (pyspark)

1. (default) ./spark/bin/pyspark --master spark://spark-master:17077 --name pyspark-pgt
2. (default) ./spark/bin/pyspark --master spark://spark-master:17077 --name pyspark-pgt --executor-cores 4 --executor-memory 1g
3. (2c, 1g) ./spark/bin/pyspark --master spark://spark-master:17077 --name pyspark-pgt --executor-cores 2 --executor-memory 1g

## spark-submit

### scala

1. ./spark/bin/spark-submit --master spark://spark-master:17077 --name spark-submit-pgt --num-executors 2 --executor-cores 4 --executor-memory 1g --class org.apache.spark.examples.SparkPi ./spark/examples/jars/spark-example*.jar 50

### python

1. ./bin/spark-submit --master spark://spark-master:17077 examples/src/main/python/pi.py 50

<!-- 2. ./spark/bin/spark-shell --master yarn --deploy-mode client --name ParkGyeongTae --class org.apache.spark.examples.SparkPi --driver-memory 1g --executor-memory 2g --num-executors 3 --executor-cores 2 ./spark/examples/jars/spark-example*.jar 50000
3. ./spark/bin/spark-submit --master yarn --deploy-mode cluster --name ParkGyeongTae --class org.apache.spark.examples.SparkPi --driver-memory 1g --executor-memory 2g --num-executors 2 --executor-cores 2 ./spark/examples/jars/spark-example*.jar 100000

- ./spark/bin/spark-submit --deploy-mode client --name ParkGyeongTae --class org.apache.spark.examples.SparkPi --driver-memory 1g --executor-memory 2g --num-executors 3 --executor-cores 2 ./spark/examples/jars/spark-example*.jar 50 -->