from django.shortcuts import render
from .models import Patient
def search(request):
    y = request.GET['idno']
    recs = Patient.objects.filter(idno=y)
    return render(request, 'patient.html', {'recs': recs})
