from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
#from datetime import datetime  # Cambio la importación aquí

def create(request):
    rep = Reporter(first_name='Nico', last_name='Duque', email="nico@gmail.com")
    rep.save()

    art1 = Article(headline='natilla es gorda', reporter=rep)
    art1.save()
    art2 = Article(headline='buñuelo es gordo', reporter=rep)
    art2.save()
    art3 = Article(headline='bigotes es gordo', reporter=rep)
    art3.save()

    #result = art1.reporter.first_name
    #result = rep.article_set.filter()
    #result = rep.article_set.filter(headline='buñuelo es gordo')
    result = rep.article_set.count()

    return HttpResponse(result)
