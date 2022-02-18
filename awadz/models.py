from django.db import models

# Create your models here.
class Profile(models.Model):
    
    bio=models.TextField()
    location=models.CharField(max_length=50)
    email=models.EmailField()
    url=models.URLField()
 
 
 
class Projects(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    urls=models.URLField()
    pub_date=models.DateTimeField(auto_now_add=True)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    voters = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    def save_project(self):
     self.save()
  
    def delete_project(self):
     self.delete()

     def voters_num(self):
         return self.voters.count()

     @classmethod
     def get_all_projects(cls):
         return cls.objects.all()

    @classmethod
    def get_project(cls,id):
        return Projects.objects.get(id=id)

    @classmethod
    def search_project(cls,name):
        return cls.objects.filter(name__icontains=name)

    @classmethod
    def user_projects(cls,profile):
        return cls.objects.filter(profile=profile)  

class Meta:
  ordering=['-pub_date']



class Ratings(models.Model):
    
    pass