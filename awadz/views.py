from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import response
from django.http.request import HttpHeaders
from django.http.response import Http404, HttpResponse
from .models import Profile, Projects, Ratings
import datetime as dt

# Create your views here.


@login_required
def index(request):
    date = dt.date.today()
    try:
        projects = Projects.get_all_projects()
    except Projects.DoesNotExist:
        raise Http404()
    project_ratings = projects.order_by('-ratings__average_rating')
    best_rating = None
    best_votes = None
    if len(project_ratings) >= 1:
        best_rating = project_ratings[0]
        ratings = Ratings.project_votes(best_rating.id)
    return render(request, 'index.html', {"date": date, "highest_vote": best_votes, "projects": projects, "highest_rating": best_rating})


@login_required
def projects(request):
    return render(request, 'projects.html')

# adding the login required requirement @login_required(login_url='/accounts/login/')
# def article(request, article_id):


@login_required
def projectdetail(request, id):

    ctx = {
        "id": id
    }

    return render(request, projectdetail.html)
