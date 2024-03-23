from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    

class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-updated','-created']
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    body=models.TextField()
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.body[:50]
    