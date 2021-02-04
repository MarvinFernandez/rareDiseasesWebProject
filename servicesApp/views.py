from django.shortcuts import render
from .models import Diseases, Resources, Url, Resourcestype

# Create your views here.

def Services(request):

    return render(request, "services/services.html")

def DiseasesTable(request):

    diseasesDB = Diseases.objects.all()

    return render(request, "services/diseases_Table.html", {"diseasesDB": diseasesDB})

def ResourcesTable(request):

    resourceDB = Resources.objects.all()
    resourceDB = resourceDB.order_by('idresources')

    return render(request, "services/resource_Table.html", {"resourceDB": resourceDB})

def ResourcesSelet(request,finality_id):

    resourceDB = Resources.objects.filter(price=finality_id)

    return render(request, "services/resource_Table.html", {"resourceDB": resourceDB})

def UrlsTable(request):

    urlDB = Url.objects.all()

    return render(request, "services/urls_Table.html", {"urlDB": urlDB})

def ResourcestypeTable(request):

    resourcestypeDB = Resourcestype.objects.all()

    return render(request, "services/resourcestype_Table.html", {"resourcestypeDB": resourcestypeDB})