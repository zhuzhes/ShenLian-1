from django.shortcuts import render
from basic_app.models import Class_Model_Model1

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def devicestatus(request):
    devicestatus = Class_Model_Model1.objects.order_by('router_name')
    devicestatus_dict = {'device_status':devicestatus}
    return render(request,'basic_app/devicestatus.html',devicestatus_dict)
