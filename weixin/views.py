import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse


def hello(request):
    # hostname = os.getenv('HOSTNAME', 'unknown')
    return HttpResponse("Hello world ! ")
    # return render(request, 'welcome/index.html', {
    #     'hostname': hostname,
    #     'database': database.info(),
    #     'count': PageView.objects.count()
    # })
