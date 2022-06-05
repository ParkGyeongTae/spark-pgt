#!/bin/bash

sleep 1

# 스파크 마스터 실행
if [ ${SPARK_MODE} == "master" ]; then
    bash /home/spark/sbin/start-master.sh --properties-file /home/spark/conf/ha.conf
    bash
fi

# 스파크 슬레이브 실행
if [ ${SPARK_MODE} == "slave" ]; then
    bash /home/spark/sbin/start-slave.sh spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT},${SPARK_MASTER_HOST_SUB}:${SPARK_MASTER_PORT_SUB} -c ${SPARK_WORKER_CORES} -m ${SPARK_WORKER_MEMORY}
    bash
fi

# 제플린 실행
if [ ${SPARK_MODE} == "zeppelin" ]; then
    bash /home/zeppelin/bin/zeppelin-daemon.sh start
    bash
fi

# 클라이언트 실행
if [ ${SPARK_MODE} == "client" ]; then
    bash
fi

# 히스토리서버 실행
if [ ${SPARK_MODE} == "history-server" ]; then
    bash /home/spark/sbin/start-history-server.sh
    bash
fi