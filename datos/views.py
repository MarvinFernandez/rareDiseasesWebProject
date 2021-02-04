from django.shortcuts import render, redirect

from .forms import FormularioContacto

# Create your views here.

def Contacto(request):

    formuario_contato=FormularioContacto()

    if request.method=="POST":
        formuario_contato=FormularioContacto(data=request.POST)
        if formuario_contato.is_valid():
            name=request.POST.get("name")
            email=request.POST.get("email")
            content=request.POST.get("content")

            return redirect("/contact/?valid")

    return render(request, "contacto/contacto.html", {'miformulario': formuario_contato})