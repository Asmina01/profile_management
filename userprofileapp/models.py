from django.contrib.auth.models import User
from django.db import models

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    email = models.EmailField(max_length=255,blank=True, null=True)
    bio = models.TextField(max_length=900,blank=True, null=True)

    contact = models.CharField(max_length=15,blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


    def __str__(self):
        return self.user.username


class Skill(models.Model):
    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} ({self.percentage}%)'



class project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    project_name=models.CharField(max_length=300,blank=True, null=True)
    link=models.CharField(max_length=100,blank=True,null=True)

    description =models.TextField(blank=True, null=True)
    image= models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.project_name





class UserProfile(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)

    def __str__(self):
        return  '{}'.format(self.username)


class loginTable(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    type=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)


