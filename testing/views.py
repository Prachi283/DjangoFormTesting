from django.shortcuts import render
from django.http import HttpResponse
from .forms import Createform
# Create your views here.
def home(request):
    if request.method=="POST":
        form=Createform(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Data is Saved")
    else:
        form=Createform()
        return render(request,'home.html',{'form':form})

def home_view(request):
    print(request.GET)
    return render(request, "home.html")

