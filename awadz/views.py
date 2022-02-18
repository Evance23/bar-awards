from django.shortcuts import render

# Create your views here.

def index(request):
    return render( request, 'index.html')


def projects(request):
    return render(request, 'projects.html')



def projectdetail(request):
    return render(request, projectdetail.html)