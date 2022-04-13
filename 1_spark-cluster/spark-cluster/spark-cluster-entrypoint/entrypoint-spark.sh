#!/bin/bash

sleep 1

# 스파크 마스터 실행
if [ ${SPARK_MODE} == "master" ]; then
    bash /home/spark/sbin/start-master.sh
fi

sleep 1

# 스파크 슬레이브 실행
if [ ${SPARK_MODE} == "slave" ]; then
    bash /home/spark/sbin/start-slave.sh spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT} -c ${SPARK_WORKER_CORES} -m ${SPARK_WORKER_MEMORY}
fi

sleep 1

bash