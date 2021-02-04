from django.shortcuts import render
from django.db.models import Q
from servicesApp.models import *
# Create your views here.

def FinderView(request):  

    return render(request, "finder/finder.html")

def Results(request):

    query_Box = request.GET["query_Box"]

    if query_Box:#si hay algo entra
        
        #disease_Results= Diseases.objects.filter(treatment=query_Box)
        #revisa cada uno de los campos de la tabla que indique  
        disease_Results= Diseases.objects.filter(
            Q(diseasename__icontains = query_Box) | 
            Q(affectedsystem__icontains = query_Box)
        ).distinct() 

    else: 
        disease_Results = Diseases.objects.all()
        query_Box=""

    disease_Results = disease_Results.order_by('diseasename')
    return render(request, "finder/results.html", {"disease_Results": disease_Results, "query" : query_Box})

def DiseasesView (request, disease_id):

    disease = Diseases.objects.get(iddisease=disease_id)
    #resources = Resources.objects.filter(resources_diseases=disease)
    resources=disease.resources_set.all()
    #urls = Url.objects.filter(idurl=resources_url)
    #if resources:
     #   for resource in resources:
      #      resources_url = ResourcesUrl.objects.get(idresource=resource.idresource) 
    return render(request, "finder/disease.html", {"disease" : disease, "resources" : resources})

def ResourceView (request, resource_id):

    resource = Resources.objects.get(idresources=resource_id)
    #purlstype=resourcesurl.resources_set.all()
    urlsobjets=resource.resources_url.all()
    resourcestype=resource.resources_resourcestype.all()
    #diseases=resource.resources_diseases.all()
    return render(request, "finder/resource.html", {"resource" : resource, "urlsobjets" : urlsobjets, "resourcestype" : resourcestype})

def ResourceTypeView (request, resourcestype_id):

    resourcestype = Resourcestype.objects.get(idtype=resourcestype_id)
    #resources = Resources.objects.filter(resources_diseases=disease)
    resources=resourcestype.resources_set.all()
    return render(request, "finder/resourcestype.html", {"resourcestype" : resourcestype, "resources" : resources})