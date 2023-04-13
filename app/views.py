from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(request):
    if request.method=='POST':
        name=request.POST['un']
        pw=request.POST['pw']
        return HttpResponse('Login successfully')
    return render(request,'hai.html')


def hello(request):
    if request.method=='POST':
        first_name=request.POST['fn']
        last_name=request.POST['ls']
        password=request.POST['pw']
        confirm_password=request.POST['cpw']
        return HttpResponse('login successfully')
    return  render(request,'hello.html')

