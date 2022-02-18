from django.urls import path
from . import views 


urlpatterns=[
    path('', views.index, name='homepage'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:id>/', views.projectdetail, name='projectdetail')
    
]