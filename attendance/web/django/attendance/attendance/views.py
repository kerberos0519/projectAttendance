###############################################
# django 관련 및 웹페이지 처리
###############################################
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import URLPattern
from django.http import HttpResponse
from django.template import loader

from datetime import datetime
import sys
sys.path.append('.')
sys.path.append('I:/AI/kjh/dev/python/src/projectAttendance/attendance')

import db

def root(request):
    return redirect('attendance/')

def index(request):
    template = loader.get_template('attendance/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def attendance_list(request):
    if request.method == 'GET':
        dtYmd = request.GET['dt']

        rows = db.selectAttendanceByDate(dtYmd)
        print(rows)

        peopleList = ['김준호', '정이', '윤예원', '김시민', '정현준', '이중석', '허호준', '정현재']

        attendanceList = []

        cnt = 0
        for name in peopleList:
            cnt += 1
            dict = {
                'no' : cnt,
                'name' : name,
                'dt' : '',
                'attendanceYn' : '-'
            }
            # (1, 'kjh', '2022-10-19 08:59:59')
            for j in rows:
                if j[1] == name:
                    dt = j[2]
                    dict['dt'] = dt
                    
                    # 저장된 dt 값이 2022-10-25 09:30:10 형식의 길이일 경우
                    if len(dt) == 19:
                        # YYYY-MM-dd 형태로 파싱
                        dtYmd = dt[0:10]
                        d1 = datetime.strptime(dtYmd +" 09:00:00", "%Y-%m-%d %H:%M:%S")
                        d2 = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
                        diff = d2 - d1
                        diffSec = diff.total_seconds()
                        print(diffSec)
                        if diffSec <= 0:
                            # 일찍 옴
                            dict['attendanceYn'] = '1'
                        else:
                            # 늦게 옴
                            dict['attendanceYn'] = '2'

                            if diffSec / 3600 >= 4:
                                # 4시간 넘으면, 결석
                                dict['attendanceYn'] = '3'
                    else:
                        pass

            attendanceList.append(dict)

        template = loader.get_template('attendance/list.html')
        context = {
            'attendanceList': attendanceList,
            'dt' : dtYmd,
        }
        return HttpResponse(template.render(context, request))

def attendance_list_json(request):
    if request.method == 'GET':
        dtYmd = request.GET['dt']

        rows = db.selectAttendanceByDate(dtYmd)
        print(rows)

        peopleList = ['김준호', '정이', '윤예원', '김시민', '정현준', '이중석', '허호준', '정현재']

        attendanceList = []

        cnt = 0
        for name in peopleList:
            cnt += 1
            dict = {
                'no' : cnt,
                'name' : name,
                'dt' : '',
                'attendanceYn' : '-'
            }
            # (1, 'kjh', '2022-10-19 08:59:59')
            for j in rows:
                if j[1] == name:
                    dt = j[2]
                    dict['dt'] = dt
                    
                    # 저장된 dt 값이 2022-10-25 09:30:10 형식의 길이일 경우
                    if len(dt) == 19:
                        # YYYY-MM-dd 형태로 파싱
                        dtYmd = dt[0:10]
                        d1 = datetime.strptime(dtYmd +" 09:00:00", "%Y-%m-%d %H:%M:%S")
                        d2 = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
                        diff = d2 - d1
                        diffSec = diff.total_seconds()
                        if diffSec <= 0:
                            # 일찍 옴
                            dict['attendanceYn'] = '1'
                        else:
                            # 늦게 옴
                            dict['attendanceYn'] = '2'

                            if diffSec / 3600 >= 4:
                                # 4시간 넘으면, 결석
                                dict['attendanceYn'] = '3'
                    else:
                        pass

            attendanceList.append(dict)

        context = {
            'attendanceList': attendanceList,
            'dt' : dtYmd,
        }
        return JsonResponse(context)

def attendance_input(request):
    if request.method == 'GET':
        name = request.GET['name']
        dt = request.GET['dt']

        resultYn = ''

        try:
            db.doAttend(name, dt)
            resultYn = 'Y'
        except :
            resultYn = 'N'

        template = loader.get_template('attendance/index.html')
        context = {
            'inputSuccYn' : resultYn
        }
        return HttpResponse(template.render(context, request))
