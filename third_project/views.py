from django.shortcuts import render

def home(request):
    return render(request, "index.html", context={"name":"anwar",'age': 23, 'marks': 40, "list":[12,23,45,67], 'blog':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora voluptatem voluptatum ipsum laboriosam totam esse consequatur commodi sit id, earum dignissimos recusandae.' })