# projectAttendance
TM을 이용한 얼굴인식 출석체크

#### 필요한 패키지 설치
    pip install opencv-python
    pip install pysqlite3
    pip install pandas
    pip install tensorflow

### 실행
###### projectAttendance/attendance 디렉토리에서
    python main.py

### 웹서버 실행
###### projectAttendance/attendance/web/django/attendance 디렉토리에서
    python manage.py runserver

###### 웹서버 실행 확인 - 인터넷 브라우저(chrome, whale ... etc)를 열고, 주소창에서
    localhost:8000