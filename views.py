from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples = [
        {'name' : 'Siddhi'},
        {'name' : 'sharvari'},
    ]
    
    return render(request,"index.html",context = {'peoples' : peoples})
def success(request):
    return HttpResponse("succes page")

def contact(request):
    return render(request ,"contact.html")