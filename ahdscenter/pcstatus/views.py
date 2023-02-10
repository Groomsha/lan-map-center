from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request) -> str:
    # return HttpResponse('APP PC Status')
    return render(request, 'index.html')
