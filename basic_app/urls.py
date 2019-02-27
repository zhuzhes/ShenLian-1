from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^RouterAdding/$',views.RouterAdding,name='RouterAdding'),
    url(r'^other/$',views.other,name='other'),
    url(r'^devicestatus/$',views.devicestatus,name='devicestatus'),

]
