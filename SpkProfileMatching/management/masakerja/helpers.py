import pandas as pd
from orm.models import Karyawan, Kecerdasan, MasaKerja, PendidikanTerakhir, Prilaku, SikapKerja 

def get_gap(df, target):
    for idx in range(0,len(df)):
        df.loc[idx] = df.loc[idx] - target
    return df

def bobot(x):
    if x == 0 : return 5
    elif x == 1 : return 4.5
    elif x == -1 : return 4
    elif x == 2 : return 3.5
    elif x == -2 : return 3 
    elif x == 3 : return 2.5
    elif x == -3 : return 2
    elif x == 4 : return 1.5
    elif x == -4 : return 1
    
def pembobotan(df, cols):
    for c in cols:
        df[c] = df[c].apply(bobot)
    return df 

#mendapatkan nilai core factor dan secondary factor
def get_cfsf(df1):
    total_column = len(df1.columns)
    cfsf = df1.sum(axis=1) / total_column
    return cfsf

#perhitungan nilai total
def result(cf, sf):
    cf = cf*0.6
    sf = sf*0.4
    total = cf + sf
    return total

def ListMasaKerjaNilai(krywn):
    if len(krywn)>0:
        target = [2,2,3,3,4,4,4,5,5]
        cols = [
            'nol_sd_empat', 'lima_sd_delapan', 'sembilan_sd_tigaenam','tigabelas_sd_enambelas',
            'tujuhbelas_sd_duapuluh','duasatu_sd_duaempat','dualima_sd_duadelapan',
            'duasembilan_sd_tigadua','tigatiga_sd_tigaenam'
        ]

        krn = {'nama': [a.nama for a in krywn]}
        dfkrn = pd.DataFrame(data=krn)

        mk = {
            cols[0] : [int(a.masakerjas.nol_sd_empat) for a in krywn],
            cols[1] : [int(a.masakerjas.lima_sd_delapan) for a in krywn],
            cols[2] : [int(a.masakerjas.sembilan_sd_tigaenam) for a in krywn],
            cols[3] : [int(a.masakerjas.tigabelas_sd_enambelas) for a in krywn],
            cols[4] : [int(a.masakerjas.tujuhbelas_sd_duapuluh) for a in krywn],
            cols[5] : [int(a.masakerjas.duasatu_sd_duaempat) for a in krywn],
            cols[6] : [int(a.masakerjas.dualima_sd_duadelapan) for a in krywn],
            cols[7] : [int(a.masakerjas.duasembilan_sd_tigadua) for a in krywn],
            cols[8] : [int(a.masakerjas.tigatiga_sd_tigaenam) for a in krywn],
        }
        dfmk = pd.DataFrame(data=mk)

        gap = get_gap(dfmk, target)
        pb = pembobotan(gap, cols)
        new = pd.concat([dfkrn, pb], axis=1)
        return new
    else:
        return []