from django.db import models

# Create your models here.


class Radios(models.Model):
    KeyRadio = models.CharField(max_length=6,unique=True)
    PACRadio = models.CharField(max_length=255)
    RadioModel = models.CharField(max_length=250,null=True,default=True)
    VersionFW = models.CharField(max_length=250,null=True,default=True)
    Protocol = models.CharField(max_length=250,null=True,default=True)

    DateCreation = models.DateTimeField(auto_now=True)
    Station = models.CharField(max_length=8,null=True)
    Data = models.CharField(max_length=250,null=True)
    Lat = models.CharField(max_length=50,null=True)
    Lng = models.CharField(max_length=50,null=True)
    Reles = models.CharField(max_length=50,null=True)
    Energia = models.CharField(max_length=50,null=True)
    Blue = models.CharField(max_length=50,null=True)
    Duplicate = models.BooleanField(default=False)
    Snr = models.CharField(max_length=50,null=True)
    AvgSnr = models.CharField(max_length=50,null=True)
    Rssi = models.CharField(max_length=50,null=True)
    SeqNumber = models.CharField(max_length=50,null=True)
    #Direccion = models.ForeignKey(Direccion)
    
    def __str__(self):
        return self.KeyRadio