# spark-pgt/0_spark-master

## 사용방법

1. 명령어 작업 위치
- /spark-pgt/0_spark-master

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

1. 스파크 마스터 컨테이너를 1개 만들어서 자유롭게 테스트