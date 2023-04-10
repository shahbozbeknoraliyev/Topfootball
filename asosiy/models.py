from django.db import models

# Create your models here.
class Club(models.Model):
    nom=models.CharField(max_length=50)
    davlat=models.CharField(max_length=50)
    logo=models.FileField()
    president=models.CharField(max_length=50)
    murabbiy=models.CharField(max_length=50)
    yil=models.DateField()
    eng_katta_t=models.FloatField()
    eng_katta_sotuv=models.FloatField()
    def __str__(self):
        return self.nom
class Player(models.Model):
    ism=models.CharField(max_length=50)
    pozitsiya=models.CharField(max_length=50)
    millat=models.CharField(max_length=50)
    tr_narx=models.FloatField()
    tug_yil=models.DateField()
    club=models.ForeignKey(Club,on_delete=models.CASCADE)
    def __str__(self):
        return self.ism
class Transfer(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    eski=models.ForeignKey(Club,on_delete=models.CASCADE,related_name="sotilgan")
    yangi=models.ForeignKey(Club,on_delete=models.CASCADE)
    narx=models.FloatField()
    tax_narx=models.FloatField()
    mavsum=models.CharField(max_length=50)
class Hozirgimavsum(models.Model):
    mavsum=models.CharField(max_length=50)