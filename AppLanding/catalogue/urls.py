from django.conf.urls import url
from catalogue import views

app_name='catalogue'
urlpatterns=[
    url(r'^architecture/$',views.architecture,name='architecture'),
]
