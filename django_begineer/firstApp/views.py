from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstApp(request):
    return render(request, 'firstApp/index.html')

def about(request):
    return HttpResponse('This is first app about page')