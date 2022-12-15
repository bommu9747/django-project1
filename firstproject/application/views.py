from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def good(request):
    return render(request,'about.html')
def new1(request):
    return render(request,'new1.html')

