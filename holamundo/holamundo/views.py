from django.http import HttpResponse

def saludo(request):
    return HttpResponse('Hola mundo')

def despedida(request):
    return HttpResponse('Hasta la proxima')

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse('Eres legal')
    else:
        return HttpResponse('Eres ilegal')