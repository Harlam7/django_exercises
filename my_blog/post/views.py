from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse

def queries(request):
    #obtener todos los emlementos
    authors = Author.objects.all()
    
    #Obtener los datos filtrados por condición
    filtered = Author.objects.filter(email='alexander10@example.net')

    #Obtener un único objeto (filtrado)
    author = Author.objects.get(id=1)

    #obtener los 10 primeros elementos
    limits = Author.objects.all()[:10]

    #obtener los 10 elementos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

     #obtener todos los emlementos
    orders = Author.objects.all().order_by('email')

    #obtener todos los elementos cuyuo id sea menor o igual a 15
    filtered2 = Author.objects.filter(id__lte = 15)

    #obtener todos los autores que contienen en su nombre la palabra a
    filtered3 = Author.objects.filter(name__contains = "a")

    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author':author,
                                                 'limits': limits, 'offsets': offsets, 'orders': orders, 'filtered2': filtered2,
                                                 'filtered3': filtered3})


def update(request):
    author = Author.objects.get(id=1)
    author.name = "Nico"
    author.email = "nico@gmail.com"
    author.save()
    return HttpResponse("modificado")
