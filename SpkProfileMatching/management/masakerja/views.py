from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages

import pandas as pd
from orm.models import Karyawan, Kecerdasan, MasaKerja, PendidikanTerakhir, Prilaku, SikapKerja 
from management.masakerja import helpers

class ListMasaKerjaView(View):
    def get(self, request):
        template = 'masakerja/index.html'
        krywn = Karyawan.objects.all()
        nlm = helpers.ListMasaKerjaNilai(krywn).as_matrix()
        data = {
            'nlm' : nlm,
        }
        return render(request, template, data)