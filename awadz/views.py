from django.shortcuts import render

# Create your views here.

def index(request):
    return render( request, 'index.html')


def projects(request):
    return render(request, 'projects.html')

# adding the login required requirement @login_required(login_url='/accounts/login/')
# def article(request, article_id):

def projectdetail(request, id):
    
    ctx = {
        "id": id 
    }
    
    return render(request, projectdetail.html)