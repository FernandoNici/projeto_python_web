from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('Hello darkness <h4>{} {}</h4>'.format(nome, idade))