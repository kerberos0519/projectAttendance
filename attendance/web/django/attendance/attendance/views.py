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
        dt = request.GET['dt']

        rows = db.selectAttendanceByDate(dt)
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
                    # 시간 계산
                    d1 = datetime.strptime("2022-10-24 09:00:00", "%Y-%m-%d %H:%M:%S")
                    d2 = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
                    diff = d1 - d2
                    if diff > 0:
                        # 일찍 옴
                        pass
                    else:
                        # 늦게 옴
                        pass
                    diffSec = diff.total_seconds()
                    if diffSec / 3600 < 1:
                        # 출석
                        # 'attendanceYn' : '1'
                        nmjDiff = diffSec % 3600

                    else:
                        # 지각
                        # 'attendanceYn' : '2'
                        pass

            attendanceList.append(dict)

        template = loader.get_template('attendance/list.html')
        context = {
            'attendanceList': attendanceList,
            'dt' : dt,
        }
        return HttpResponse(template.render(context, request))

def attendance_list_json(request):
    if request.method == 'GET':
        dt = request.GET['dt']

        rows = db.selectAttendanceByDate(dt)
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

            attendanceList.append(dict)

        context = {
            'attendanceList': attendanceList,
            'dt' : dt,
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
