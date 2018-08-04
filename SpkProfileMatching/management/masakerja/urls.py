from django.conf.urls import url
from management.masakerja import views


urlpatterns = [
    url (r'^$', views.ListMasaKerjaView.as_view(), name='view'),
]