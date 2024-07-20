from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse

def receipe(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')

        if not description:
            # Provide a default value if description is missing
            description = "No description provided."

        print(name)
        print(description)
        print(image)

        Receipe.objects.create(
            name=name,
            description=description,
            image=image,
        )
    #return redirect('/receipe/')
    queryset = Receipe.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        queryset = queryset.filter(name__icontains=search_query)

    context = { 'receipe' : queryset}

    return render(request, 'receipe.html',context)

def delete(request, id):
    
    queryset = Receipe.objects.get(id=id)
    context = { 'receipe' : queryset}
    queryset.delete()

    return redirect('/receipe/')

def update(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')

        if not description:
            description = "No description provided."

        queryset.name = name
        queryset.description = description
        if image:
            queryset.image = image

        queryset.save()
        return redirect('/receipe/')

    context = {'receipe': queryset}
    return render(request, 'update.html', context)


    
    



