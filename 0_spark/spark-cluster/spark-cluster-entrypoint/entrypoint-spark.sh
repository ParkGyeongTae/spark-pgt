#!/bin/bash

sleep 1

# 스파크 마스터 실행
if [ ${SparkMode} == "master" ]; then
    bash /home/spark/sbin/start-master.sh
fi

sleep 1

# 스파크 슬레이브 실행
if [ ${SparkMode} == "slave" ]; then
    bash /home/spark/sbin/start-slave.sh spark://spark-master:17077 -c ${SparkSlaveCore} -m ${SparkSlaveMemory}
fi

sleep 1

bash