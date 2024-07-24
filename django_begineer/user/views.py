from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    usersDetails= User.objects.all()
    return render(request,'user/index.html',{'users':usersDetails})

# one way of getting user details


# def user_detail(request,user_id):
#     user=User.objects.get(pk=user_id)
#     return render(request,'user/user_detail.html',{'user':user})

# another way of getting user details

def user_detail(request,user_id):
    user=get_object_or_404(User,pk=user_id)
    return render(request,'user/user_detail.html',{'user':user})

def create_user(request):
    return render(request,'user/create_user.html')