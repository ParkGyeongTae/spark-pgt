#!/bin/bash

sleep 1

# 스파크 마스터 실행
if [ ${SPARK_MODE} == "master" ]; then
    bash /home/spark/sbin/start-master.sh --properties-file /home/spark/ha.conf
    # bash /home/spark/sbin/start-master.sh -p ${} --webui-port ${} --properties-file /home/spark/ha.conf
fi

sleep 1

# 스파크 슬레이브 실행
if [ ${SPARK_MODE} == "slave" ]; then
    bash /home/spark/sbin/start-slave.sh spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT},${SPARK_MASTER_HOST_SUB}:${SPARK_MASTER_PORT_SUB} -c ${SPARK_WORKER_CORES} -m ${SPARK_WORKER_MEMORY}
fi

sleep 1

# 제플린 실행
if [ ${SPARK_MODE} == "zeppelin" ]; then
    bash /home/zeppelin/bin/zeppelin-daemon.sh start
fi

sleep 1

bash