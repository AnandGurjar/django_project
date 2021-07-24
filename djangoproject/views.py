from django.shortcuts import render
from django.http import HttpResponse

def do_calculation(value1,value2):
	return value1*value2

def test_function(request):
	tot = do_calculation(10,2)
	p_fla = True
	people = ['Gregory','Mary','Jose','Pedro','John']
	return render(request,'index.html',{'total' : tot,'people' : people, 'p_fla': p_fla})

def anand(request):
	return render(request,'index2.html')
    

def list_clients(request):
	return HttpResponse('hello world')

def special_case(request,year):
	return HttpResponse('returning articles from %s'%year)