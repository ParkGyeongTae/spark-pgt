# 실행 예시

## spark-shell

- ./spark/bin/spark-shell --master spark://spark-master:17077 --name spark-shell-pgt

- ./spark/bin/spark-shell --master spark://spark-master:17077 --name spark-shell-pgt --executor-cores 4 --executor-memory 1g

## spark-submit

- ./spark/bin/spark-submit --master spark://spark-master:17077 --name spark-submit-pgt --num-executors 2 --executor-cores 4 --executor-memory 1g --class org.apache.spark.examples.SparkPi ./spark/examples/jars/spark-example*.jar 50

- ./spark/bin/spark-shell --master yarn --deploy-mode client --name ParkGyeongTae --class org.apache.spark.examples.SparkPi --driver-memory 1g --executor-memory 2g --num-executors 3 --executor-cores 2 ./spark/examples/jars/spark-example*.jar 50000

- ./spark/bin/spark-submit --master yarn --deploy-mode cluster --name ParkGyeongTae --class org.apache.spark.examples.SparkPi --driver-memory 1g --executor-memory 2g --num-executors 2 --executor-cores 2 ./spark/examples/jars/spark-example*.jar 100000

- ./spark/bin/spark-submit --deploy-mode client --name ParkGyeongTae --class org.apache.spark.examples.SparkPi --driver-memory 1g --executor-memory 2g --num-executors 3 --executor-cores 2 ./spark/examples/jars/spark-example*.jar 50