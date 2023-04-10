from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('clubs/', club),
    path('players/', players),
    path('stats/', stats),
    path('stats/transfer_record/', transfer_record),
    path('latest/', latesttransfer),
    path('country/<str:pk>/', latesttransfer),
    path('playersu20/', u20players),
    path('mavsumlar/', hammamavsumlar),

]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
