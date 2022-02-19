from django.urls import path, re_path
from . import views 


urlpatterns=[
    path('', views.index, name='homepage'),
    path('signup/',views.signup,name='signup'),
     path('new_project/',views.new_project,name='new_project'),
      path('email/', views.welcome_mail, name='welcome'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:id>/', views.projectdetail, name='projectdetail'),
    path('profile/<int:profile_id>/',views.profile,name='profile'),
    re_path('rate_project/(?P<project_id>\d+)',views.rate_project,name = 'rate_project'),
    re_path('update_profile/(?P<profile_id>\d+)',views.update_profile,name='update_profile'),
   
    
]