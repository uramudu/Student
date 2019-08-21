from django.db import models
class Patient (models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    Hb=models.CharField(max_length=30)
    GlbLevel=models.CharField(max_length=30)
    HlBac=models.CharField(max_length=30)
    Heatbeet=models.CharField(max_length=30)
    Oxeygenlevel=models.CharField(max_length=30)
    Bmi=models.CharField(max_length=30)
    def __str__(self):
        return str(self.idno)


