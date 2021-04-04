from django.shortcuts import render, redirect

from .forms import FormularioContacto


from django.core.mail import EmailMessage

# Create your views here.

def Contacto(request):

    formuario_contato=FormularioContacto()

    if request.method=="POST":
        formuario_contato=FormularioContacto(data=request.POST)
        if formuario_contato.is_valid():
            name=request.POST.get("name")
            email=request.POST.get("email")
            content=request.POST.get("content")


            email = EmailMessage("Rare Diseases web project django",#Asunto
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(name,email,content),
            "",["marvinchutacabras@gmail.com"],reply_to=[email])

            try:
                email.send() 

                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?nonvalid")

    return render(request, "contacto/contacto.html", {'miformulario': formuario_contato})