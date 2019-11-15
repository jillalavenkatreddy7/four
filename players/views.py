from django.shortcuts import render

# Create your views here.
def showCricketers(req):
    return render(req,"show.html")
def getCricketers(req):
    crick2=req.POST.getlist("c")
    return render(req,"images.html",{"crck":crick2,"crck1":crick2,"crck2":crick2})




