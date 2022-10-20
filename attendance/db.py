#######################
# DB 관련 처리 파일
#######################
import sqlite3
import pandas as pd
import commonutil

# DB 관련 파일

# db 열기
def dbOpen():
    # DB 연결
    global conn;
    conn = sqlite3.connect(commonutil.getRootPath() +"/db/attendance.db")
     # 커서 가져오기
    global cur;
    cur = conn.cursor()

# db 닫기
def dbClose():
    conn.close()

# 테이블 생성
def createAttendanceTable():
    # print('[Start] create table')
    dbOpen()

    query =  'create table if not exists attendance ('
    query += 'id integer primary key autoincrement,'
    query += 'name text,'
    query += 'create_dt text,'
    query += 'update_dt text'
    query += ')'
    # print('\tQuery : '+query)
    conn.execute(query)
    dbClose()
    # print('[End] create table')
# 테이블 드랍(삭제)
def dropAttendanceTable():
    # 테이블이 있을 경우, 드랍
    print('[Start] drop table')
    
    dbOpen()

    try:
        query = 'drop table attendance'
        print('\tQuery : '+ query)
        conn.execute(query)
    except sqlite3.OperationalError as e:
        print("Already exist table. Cause :")
        print(e)

    dbClose()
    print('[End] drop table')

# 출석 데이터 추가
def insertAttendance(name):
    dbOpen()

    print('[Start] insert table')
    query = "INSERT INTO attendance (name, create_dt)VALUES ('"+ name +"', '"+ commonutil.getNowDate() +"')"
    print('\tQuery : '+ query)
    cur.execute(query)
    
    '''
    # 한번에 여러개의 행을 입력하고 싶을때...
    cur.executemany(
        'INSERT INTO attendance VALUES (?, ?, ?)',
        [
            (1, 'kjh', '2022-10-12 00:00:00.000'), 
            (2, 'jhj', '2022-10-12 00:00:00.000')
        ]
    )
    '''
    # db 저장
    conn.commit()
    dbClose()
    print('[End] insert table')

# 출석 데이터 추가
def insertAttendanceTest(name, dt):
    dbOpen()

    print('[Start] insert table')
    query = "INSERT INTO attendance (name, create_dt) VALUES ('"+ name +"', '"+ dt +"')"
    print('\tQuery : '+ query)
    cur.execute(query)
    
    # db 저장
    conn.commit()
    dbClose()
    print('[End] insert table')

# 출석 데이터 수정(쓸일이 있을려나)
def updateAttendance(id, name):
    dbOpen()

    # print('[Start] update table')
    query = "update attendance set name='"+ name +"', update_dt='"+ commonutil.getNowDate() +"' where id="+ str(id)
    # print('\tQuery : '+ query)
    cur.execute(query)
    # db 저장
    conn.commit
    # print('[End] update table')

    dbClose()
    
# 모든 출석 데이터 들고 오기
def selectAttendanceAll():
    dbOpen()

    query = "SELECT * FROM attendance"
    cur.execute(query)
    print('\tQuery : '+ query)
    rows = cur.fetchall()

    cols = [column[0] for column in cur.description]
    data_df = pd.DataFrame.from_records(data=rows, columns=cols)
    print('#########################################')
    print(data_df)
    print('#########################################')
    '''
    for row in rows:
        print(row)
    '''
    dbClose()

# 하나의 출석 데이터 들고오기
# ex> (1, 'kjh', '2022-10-19 09:32:28', None)
def selectAttendanceOne(name, dateYmd):
    dbOpen()
    query = "SELECT * "
    query += "FROM attendance "
    query += "WHERE 1=1 "
    query += "AND name='"+ name +"'"
    query += "AND date(create_dt)='"+ dateYmd +"'"

    cur.execute(query)
    print('\tQuery : '+ query)
    row = cur.fetchone()
    # print(row)

    dbClose()

    return row

# 해당 날짜의 출석 데이터 들고오기
# ex> (1, 'kjh', '2022-10-19 09:32:28', None), ...
def selectAttendanceByDate(dateYmd):
    dbOpen()

    query = "SELECT * "
    query += "FROM attendance "
    query += "WHERE 1=1 "
    query += "AND date(create_dt)='"+ dateYmd +"'"

    cur.execute(query)
    print('\tQuery : '+ query)
    rows = cur.fetchall()
    # print(row)

    dbClose()

    return rows

# 이미 출석했는지 확인
def isAttended(name, dateYmd):
    dbOpen()

    # 출석 대상을 먼저 검색
    tplRow = selectAttendanceOne(name, dateYmd)
    dbClose()

    # 출석 대상이 있으면?
    if tplRow != None:
        # 출석 대상 있으면
        return True
    else:
        # 없다면 리턴
        return False
    
# 출석시키기
def doAttend(name, dt):
    dbOpen()

    # 출석 여부 판별
    if isAttended(name, dt) == False:
        # db에 넣기
        insertAttendanceTest(name, dt)
    else :
        raise Exception('Alreay exist in today')

    dbClose()

# test
def test():
    createAttendanceTable()
    insertAttendance("kjh")
    # updateAttendance(1, "hgd")
    selectAttendanceOne('kjh', '2022-10-19')
