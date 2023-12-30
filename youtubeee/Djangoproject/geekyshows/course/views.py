from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse('Home page')

def learn_django(request):
    return HttpResponse('hello django')


# def learn_python(request):
#     return HttpResponse('hello python')


# def learn_var(request):
#     a='<h1>hello python</h1>'
#     return HttpResponse(a)


# def learn_math(request):
#     a=10+10
#     return HttpResponse(a)

# def learn_format(request):
#     a=20+30
#     return HttpResponse(f'your some is {a}')
