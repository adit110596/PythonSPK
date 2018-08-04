from django.conf.urls import url
from management.kecerdasan import views

urlpatterns = [
    url (r'^$', views.ListKecerdasanView.as_view(), name='view'),
    url (r'^cf$', views.ListCfView.as_view(), name='cf'),

]