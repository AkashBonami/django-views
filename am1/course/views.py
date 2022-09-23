from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):

    return render(request , 'index.html',{'name': 'my name is akash'})
def learn_python(request):
     names = {'name':['akash','vivek','arya']}
     return render(request , 'index.html',{'name':['akash','vivek','arya']})

