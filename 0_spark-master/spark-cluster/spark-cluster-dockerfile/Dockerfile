FROM ubuntu:18.04
LABEL maintainer "ParkGyeongTae"

# apt 설치시 입력요청 무시
ENV DEBIAN_FRONTEND=noninteractive

# apt 미러서버 미국(default) -> 한국 변경
RUN sed -i 's@archive.ubuntu.com@kr.archive.ubuntu.com@g' /etc/apt/sources.list

# 자주 사용하는 패키지 설치
RUN apt-get clean && \
    apt-get update && \
    apt-get install net-tools -y && \
    apt-get install iputils-ping -y && \
    apt-get install vim -y && \
    apt-get install wget -y

# 작업영역 /home
WORKDIR /home

# jdk
RUN apt-get install openjdk-8-jdk -y

# spark-3.2.1-bin-hadoop3.2
RUN wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz && \
    tar -xvf spark-3.2.1-bin-hadoop3.2.tgz && \
    mv spark-3.2.1-bin-hadoop3.2 spark && \
    rm -rf spark-3.2.1-bin-hadoop3.2.tgz

# python 3.8.0
RUN apt-get install python3.8 -y && \
    ln -s /usr/bin/python3.8 /usr/bin/python3 && \
    ln -s /usr/bin/python3.8 /usr/bin/python

# pip3 설정
RUN mkdir /root/.pip && \
    set -x \
    && { \
    echo '[global]'; \
    echo 'timeout = 60'; \
    echo '[freeze]'; \
    echo 'timeout = 10'; \
    echo '[list]'; \
    echo 'format = columns'; \
    } > /root/.pip/pip.conf

# 환경설정
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV SPARK_HOME /home/spark
ENV PATH $PATH:$JAVA_HOME/bin:$SPARK_HOME/bin

# spark 설정파일 수정
# COPY ./spark-cluster/spark-cluster-conf/spark-env.sh /home/spark/conf/spark-env.sh

# RUN rm -rf /home/spark/conf/spark-env.sh.template && \
#     rm -rf /home/spark/bin/*.cmd

# 컨테이너 실행시 spark 자동실행
COPY ./spark-cluster/spark-cluster-entrypoint/entrypoint-spark.sh /usr/local/bin/

ENTRYPOINT ["entrypoint-spark.sh"]