from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect

User = get_user_model() 

def signup(request):
    if request.method == "POST": # Traitement du formulaire 
                     
        username = request.POST.get("username") #|____| ecuperation des info du formulaire
        password = request.POST.get("password") #|
        user = User.objects.create_user(username=username, password=password)
                                         

        login(request, user) #connexion au site
        return redirect('index') # rediriger vers la page daccueil


    return render(request, 'accounts/signup.html')