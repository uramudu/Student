from django.contrib import admin
from .models import Patient
class Patientadmin(admin.ModelAdmin):
    list_display = ['idno', 'name', 'Hb','GlbLevel','HlBac','Heatbeet','Oxeygenlevel','Bmi']
    list_filter = ['idno', 'name', 'Hb','GlbLevel','HlBac','Heatbeet','Oxeygenlevel','Bmi']
    class meta:
     model=Patient
admin.site.register(Patient,Patientadmin)
