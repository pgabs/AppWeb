from django.shortcuts import render
from django.http import HttpResponse



#def index(request):
    #return HttpResponse('Olá Mundo!')

def index(request): return render(request, "index.html") 

def contato(request):
    if request.method == "GET":
        print (request.POST.get('name'))
        print (request.POST.get('email'))
        return render(request,'contato.html')

def login(request):
    if request.method == "GET":
        print ("Acesso via GET")
        return render(request,"login.html")
    elif request.method =="POST":
        print ("Acesso via POST")
        email= request.POST.get ("email")
        if request.POST.get ("senha")=="teste123":
            print ('Usuario {} entrou com sucesso!'.format (email))
            return render (request,"index.html")
        else:
            print ('Usuario {} digitou a senha errada!'.format (email))
        return render (request,"login.html")