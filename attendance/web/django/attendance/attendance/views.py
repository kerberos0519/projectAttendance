

from django.http import HttpResponse
from django.urls import URLPattern
from django.http import HttpResponse
from django.template import loader

import sys

sys.path.append('.')

def index(request):
    template = loader.get_template('attendance/index.html')
    context = {
        'list_test': ['a', 'b', 'c', 'd'],
    }
    return HttpResponse(template.render(context, request))

def attendance_list(request):
    template = loader.get_template('attendance/list.html')
    context = {
        'attendanceList': [
            {'no':1, 'name':'kjh', 'create_dt':'2022-10-19 08:59:59'},
            {'no':2, 'name':'kjs', 'create_dt':'2022-10-19 08:45:34'},
            {'no':3, 'name':'jhj', 'create_dt':'2022-10-19 08:40:15'},
            {'no':4, 'name':'yyw', 'create_dt':'2022-10-19 08:30:12'},
            {'no':5, 'name':'ljs', 'create_dt':'2022-10-19 08:35:20'}
        ],
    }
    return HttpResponse(template.render(context, request))