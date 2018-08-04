from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages

import pandas as pd
from orm.models import Karyawan, Kecerdasan, MasaKerja, PendidikanTerakhir, Prilaku, SikapKerja 
from management.kecerdasan import helpers

class ListKecerdasanView(View):
    def get(self, request):
        template = 'kecerdasan/index.html'
        krywn = Karyawan.objects.all()
        nl = helpers.ListKecerdasanNilai(krywn).as_matrix()
        data = {
            'nl' : nl,
        }
        return render(request, template, data)

class ListCfView(View):
    def get(self, request):
        template = 'kecerdasan/cf.html'
        krywn = Karyawan.objects.all()
        cf = helpers.CfKecerdasan(krywn).as_matrix()
        data = {
            'cf' : cf,
        }
        return render(request, template, data)
