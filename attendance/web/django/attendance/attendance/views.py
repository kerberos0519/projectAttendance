from django.http import HttpResponse
from django.urls import URLPattern
from django.http import HttpResponse
from django.template import loader

import sys
sys.path.append('.')
sys.path.append('D:/AI/dev/python/src/projectAttendance/attendance')

import db

def index(request):
    template = loader.get_template('attendance/index.html')
    context = {
        'list_test': ['a', 'b', 'c', 'd'],
    }
    return HttpResponse(template.render(context, request))

def attendance_list(request):
    if request.method == 'GET':
        dt = request.GET['dt']

        rows = db.selectAttendanceByDate(dt)
        print(rows)

        template = loader.get_template('attendance/list.html')
        context = {
            'attendanceList': rows,
            'dt' : dt
        }
        return HttpResponse(template.render(context, request))

    '''
        [
            {'no':1, 'name':'kjh', 'create_dt':'2022-10-19 08:59:59'},
            {'no':2, 'name':'kjs', 'create_dt':'2022-10-19 08:45:34'},
            {'no':3, 'name':'jhj', 'create_dt':'2022-10-19 08:40:15'},
            {'no':4, 'name':'yyw', 'create_dt':'2022-10-19 08:30:12'},
            {'no':5, 'name':'ljs', 'create_dt':'2022-10-19 08:35:20'}
        ]
    '''

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
