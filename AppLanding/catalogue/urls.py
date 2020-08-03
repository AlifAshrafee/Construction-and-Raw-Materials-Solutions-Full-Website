from django.conf.urls import url
from catalogue import views

app_name='catalogue'
urlpatterns=[
    url(r'^architecture/$',views.architecture,name='architecture'),
    url(r'^complete/$',views.complete,name='complete'),
    url(r'^construction/$',views.construction,name='construction'),
    url(r'^engineering/$',views.engineering,name='engineering'),
    url(r'^rawMaterials/$',views.rawMaterials,name='rawMaterials'),
]
