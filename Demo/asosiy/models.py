from django.db import models

class Xodim(models.Model):
    ism = models.CharField(max_length=30)
    kasb = models.CharField(max_length=30)
    yosh = models.PositiveIntegerField()
    oylik = models.PositiveIntegerField()
    def __str__(self):
        return self.ism


class Futbolchi(models.Model):
    ism = models.CharField(max_length=25)
    transfer_narx = models.PositiveIntegerField()
    yosh = models.PositiveIntegerField()
    klub = models.CharField(max_length=30)
    nafaqada = models.BooleanField()
    def __str__(self):
        return self.ism
class Kurs(models.Model):
    nom = models.CharField(max_length=12)
    yonalish = models.CharField(max_length=15)
    daraja = models.IntegerField()
    davomiylik = models.TimeField()
    def __str__(self):
        return self.nom



class Talaba(models.Model):

    ism = models.CharField(max_length=23, unique=True)
    yosh = models.PositiveIntegerField()
    email = models.EmailField()
    jins = models.CharField(max_length=15)
    bitiruvchi = models.BooleanField()

    class Meta:
        unique_together = ['ism', 'email']

    def __str__(self):
        return self.ism

class Foydalanuvchi(models.Model):
    class Foydalanuvchi(models.Model):
        username = models.CharField(max_length=30)
        login = models.CharField(max_length=30)
        parol = models.CharField(max_length=30)
        kiritilgan_sana = models.DateField()
        def __str__(self):
            return self.username

class Universitet(models.Model):
    nom = models.CharField(max_length=100)
    talaba_soni = models.PositiveIntegerField()
    ochilgan_sanasi = models.DateField()
    sayt = models.URLField()
    yillik = models.CharField(max_length=10)
    def __str__(self):
        return self.nom


class Nashriyot(models.Model):
    nom = models.CharField(max_length=24)
    manzil = models.CharField(max_length=30)
    def __str__(self):
        return self.nom

class Kitob(models.Model):
    nom = models.CharField(max_length=100)
    narx = models.CharField(max_length=50)
    kelgan_sana = models.DateField()
    nashriyot = models.ForeignKey(Nashriyot, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Sotuvchi(models.Model):
    ism = models.CharField(max_length=20)
    tel = models.CharField(max_length=15)
    def __str__(self):
        return self.ism

class Sotuv(models.Model):
    sana = models.DateField()
    kitob_fk = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    sotuvchi  = models.ForeignKey(Sotuvchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.kitob_fk


