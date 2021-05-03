from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from servicesApp.models import * #importa las tablas de la base de datos creada especificada en el archivo models de servicesApp
# Create your views here.

def FinderView(request):  

    return render(request, "finder/browser.html")

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



def DiseaseBrowserView(request):  

    return render(request, "diseases/diseasesBrowser.html")

def ResourceBrowserView(request):  

    return render(request, "resource/resourceBrowser.html")

def ResourcestypeBrowserView(request):  

    return render(request, "resourcestype/resourcestypeBrowser.html")

def UrlBrowserView(request):  

    return render(request, "urls/urlBrowser.html")



def DiseaseResultsView(request):

    query_Box = request.GET["query_Box"]

    if query_Box:#si hay algo entra
        
        #disease_Results= Diseases.objects.filter(treatment=query_Box)
        #revisa cada uno de los campos de la tabla que indique  
        disease_Results= Diseases.objects.filter(
            Q(diseasename__icontains = query_Box) | 
            Q(affectedsystem__icontains = query_Box)| 
            Q(prevalence__icontains = query_Box)| 
            Q(treatment__icontains = query_Box)| 
            Q(diagnosis__icontains = query_Box)| 
            Q(description__icontains = query_Box)
            
        ).distinct() 

    else: 
        disease_Results = Diseases.objects.all()
        query_Box=""

    disease_Results = disease_Results.order_by('diseasename')
    return render(request, "diseases/diseasesResults.html", {"disease_Results": disease_Results, "query" : query_Box})

def ResourceResultsView(request):

    query_Box = request.GET["query_Box"]

    if query_Box:#si hay algo entra
        
        #disease_Results= Diseases.objects.filter(treatment=query_Box)
        #revisa cada uno de los campos de la tabla que indique  
        resource_Results= Resources.objects.filter(
            Q(name__icontains = query_Box) | 
            Q(finality__icontains = query_Box)| 
            Q(price__icontains = query_Box)| 
            Q(access__icontains = query_Box)
        ).distinct() 

    else: 
        resource_Results = Resources.objects.all()
        query_Box=""

    resource_Results = resource_Results.order_by('name')
    return render(request, "resource/resourceResults.html", {"resource_Results": resource_Results, "query" : query_Box})

def ResourcestypeResultsView(request):

    query_Box = request.GET["query_Box"]

    if query_Box:#si hay algo entra
        
        #disease_Results= Diseases.objects.filter(treatment=query_Box)
        #revisa cada uno de los campos de la tabla que indique  
        resourcestype_Results= Resourcestype.objects.filter(
            Q(Type__icontains = query_Box) | 
            Q(description__icontains = query_Box)
        ).distinct() 

    else: 
        resourcestype_Results = Resourcestype.objects.all()
        query_Box=""

    resourcestype_Results = resourcestype_Results.order_by('Type')
    return render(request, "resourcestype/resourcestypeResults.html", {"resourcestypeDB": resourcestype_Results, "query" : query_Box})

def UrlResultsView(request):

    query_Box = request.GET["query_Box"]

    if query_Box:#si hay algo entra
        
        #disease_Results= Diseases.objects.filter(treatment=query_Box)
        #revisa cada uno de los campos de la tabla que indique  
        url_Results= Url.objects.filter(
            Q(language__icontains = query_Box) | 
            Q(location__icontains = query_Box)| 
            Q(address__icontains = query_Box)
        ).distinct() 

    else: 
        url_Results = Url.objects.all()
        query_Box=""

    url_Results = url_Results.order_by('location')
    return render(request, "urls/urlResults.html", {"urlDB": url_Results, "query" : query_Box})

