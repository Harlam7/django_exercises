from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test(request):
    return HttpResponse("Funciona melo")

def create(request):
    #comment = Comment(name="Nico", score=5, comments="este es un comentario jeje")
    #comment.save()

    comment = Comment.objects.create(name="juli")
    return HttpResponse("Funciona melo la ruta create")

def delete(request):
    #comment = Comment.objects.get(id=1)
    #comment.delete()
    Comment.objects.filter(id=2).delete()
    return HttpResponse("Ruta para probar los borrados")
