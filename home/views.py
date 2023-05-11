from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
def index(request):
    return render(request, "index.html")
    #return HttpResponse("This is homepage")

def company(request):
    return render(request, "company.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
        contact = Contact(name=name, email=email, query= query)
        contact.save()
    return render(request, "contact.html")
def career(request):
    return render(request, "career.html")



