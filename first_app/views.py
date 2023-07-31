from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    #return HttpResponse("this is a contact page")
    return render(request, "hello.html", {'courses':[
        {
            "id":1,
            "name":"phiton",
            "instuctor":"karim",
        },
        {
            "id":13,
            "name":"phiton",
            "instuctor":"rarim",
        },
        {
            "id":23,
            "name":"phiton",
            "instuctor":"arim",
        },
    ]})