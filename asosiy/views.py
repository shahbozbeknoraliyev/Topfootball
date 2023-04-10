from django.shortcuts import render
from .models import *
# Create your views here.
def home (request):
    return render (request,"index.html")
def about(request):
    return render(request,"about.html")
def club(request):
    data={
        "clubs":Club.objects.all()
    }
    return render(request,'clubs.html',data)
def players(request):
    data={
        "players":Player.objects.all()
    }
    return render(request,"players.html",data)
def stats(request):
    return render(request,"stats.html")
def transfer_record(request):
    data={
        "transfer_r":Transfer.objects.filter(tax_narx__gt=50)[0:100]
    }
    return render(request,"transfer-records.html",data)
def latesttransfer(request):
    data={
        "trans":Transfer.objects.filter(mavsum="17/18")
    }
    return render(request,"latest-transfers.html",data)
def england(request,pk):
    data={"davlat":Club.objects.filter(davlat=pk),
          }
    return render(request,"england.html",data)
def u20players(request):
    from datetime import date,timedelta
    bugun=date.today()
    boshi=bugun-timedelta(days=(365*20)+5)
    data={
        "player":Player.objects.filter(tug_yil__range=[boshi,bugun]).order_by("-tr_narx","tug_yil"),
        "bugun":bugun.year

    }
    return render(request,"U-20 players.html",data)
def hammamavsumlar(request):
    h_mavsum=Hozirgimavsum.objects.last().mavsum
    data={
        "transfer":Transfer.objects.filter(mavsum__lt=h_mavsum).values("mavsum").distinct().order_by("-mavsum")
    }
    return render(request,"transfer-archive.html",data)