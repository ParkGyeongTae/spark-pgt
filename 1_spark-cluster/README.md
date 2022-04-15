# spark-pgt/1_spark-cluster

## 사용방법

1. 명령어 작업 위치
- /spark-pgt/1_spark-cluster

2. 도커 이미지 만들기
- ./full_build.sh

3. 컨테이너 생성
- docker-compose up -d

4. 컨테이너 접속
- ./bash/bash-spark-master.sh

5. 컨테이너 삭제
- docker-compose down

6. 이미지 삭제
- ./remove-image.sh

## 활용

1. 스파크 마스터 컨테이너를 1개 + 스파크 슬레이브 컨테이너 3개를 만들어서 자유롭게 테스트