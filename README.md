# projectAttendance
TM을 이용한 얼굴인식 출석체크

#### 필요한 패키지 설치
    pip install opencv-python
    pip install pysqlite3
    pip install pandas
    pip install tensorflow
    (선택1. django)
    pip install django
    (선택2. fastapi)
    pip install fastapi
    pip install "uvicorn[standard]"

#### 수정되어야할 부분(자신의 경로에 맞게 수정) - [향후, 수정 예정]
###### projectAttendance/attendance/commonutil.py 파일에서
    9행  : rootPath = "I:/AI/kjh/dev/python/src/projectAttendance/attendance"
###### projectAttendance/attendance/web/django/attendance/attendance
    23행 : SECRET_KEY = '발급받은 키 넣어야함'
###### projectAttendance/attendance/web/django/attendance/attendance
    11행 : sys.path.append('D:/AI/dev/python/src/projectAttendance/attendance')

### 실행
###### projectAttendance/attendance 디렉토리에서
    python main.py

### 웹서버 실행
##### 1) djnago
###### projectAttendance/attendance/web/django/attendance 디렉토리에서
    python manage.py runserver

##### 2) FastAPI
###### projectAttendance/attendance/web/fastapi 디렉토리에서
    uvicorn main:app --reload
    
###### (공통) 웹서버 실행 확인 - 인터넷 브라우저(chrome, whale ... etc)를 열고, 주소창에서
    localhost:8000