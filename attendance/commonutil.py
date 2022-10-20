##########################
# 공통 유틸 모아놓은 파일
##########################
import datetime

# 프로젝트 파일 경로 - 루트 폴더 
def getRootPath():
    # input your project path
    rootPath = "I:/AI/kjh/dev/python/src/Teachable-Machine/attendance"
    return rootPath

# 현재 시간 가져오기 - ex> 2022-10-14 09:32:15
def getNowDate():
    # 현재시간
    now = datetime.datetime.now()
    # 날짜 형식 지정
    dateFormat = "%Y-%m-%d %H:%M:%S"
    formattedDate = now.strftime(dateFormat)

    return formattedDate

# 현재 시간 가져오기 - ex> 2022-10-19
def getNowDateYmd():
    # 현재시간
    now = datetime.datetime.now()
    # 날짜 형식 지정
    dateFormat = "%Y-%m-%d"
    formattedDate = now.strftime(dateFormat)

    return formattedDate

