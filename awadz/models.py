from django.db import models

# Create your models here.
class Profile(models.Model):
    
    bio=models.TextField()
    location=models.CharField(max_length=50)
    email=models.EmailField()
    url=models.URLField()
 
 
 
class Projects(models.Model):
    
    pass 



class Ratings(models.Model):
    
    pass