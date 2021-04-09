from django.shortcuts import render, redirect

from .forms import FormularioContacto


from django.core.mail import EmailMessage

# Create your views here.

def Contacto(request):

    formulario_contato=FormularioContacto()

    if request.method=="POST":
        formulario_contato=FormularioContacto(data=request.POST)
        if formulario_contato.is_valid():
            name=request.POST.get("name")
            email=request.POST.get("email")
            content=request.POST.get("content")


            email = EmailMessage("Rare Diseases web project Django",#Asunto
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(name,email,content),
            "",["rdiseaseswebproject@gmail.com"],reply_to=[email])

            try:
                email.send() 

                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?nonvalid")

    return render(request, "contacto/contacto.html", {'miformulario': formulario_contato})
