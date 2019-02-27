from django.shortcuts import render
from basic_app.models import Class_Model_Model1
from basic_app import forms
from . import routeros_func
import time

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def other(request):
    return render(request,'basic_app/other.html')


def RouterAdding(request):
    # routeros_func.Router1()
    form = forms.Class_Form_1()
    if request.method == 'POST':
        form = forms.Class_Form_1(request.POST)

        if form.is_valid():
            #do something here
            print ("validation success")
            print("routerIP: " + form.cleaned_data["routerip"])
            print("Username: " + form.cleaned_data["username"])
            print("Password: " + form.cleaned_data["password"])
            routeros_func.Router1(router_ip=form.cleaned_data["routerip"],
                                  username=form.cleaned_data["username"],
                                  password=form.cleaned_data["password"])
            print("Router informanation fetched")
            time.sleep(3)
            return render(request,'basic_app/devicestatus.html')

    return render(request,'basic_app/RouterAdding.html',{'form':form})

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def devicestatus(request):
    devicestatus = Class_Model_Model1.objects.order_by('router_name')
    devicestatus_dict = {'device_status':devicestatus}
    return render(request,'basic_app/devicestatus.html',devicestatus_dict)
