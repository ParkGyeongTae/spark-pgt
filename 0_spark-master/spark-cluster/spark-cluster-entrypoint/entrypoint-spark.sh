#!/bin/bash

sleep 1

# 스파크 마스터 실행
if [ ${SPARK_MODE} == "master" ]; then
    bash /home/spark/sbin/start-master.sh
fi

sleep 1

bash