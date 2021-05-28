from django.db import models
from datetime import datetime
import re
import bcrypt
from apps.login_register_app.models import User

# Create your models here.
class jobManager(models.Manager):
            
    def info_Validator(self, postDATA):
        errors={}
        if len(postDATA['title'])<3:
            errors['title']="Title must have more than 2 characters"
        if len(postDATA['desc'])<3:
            errors['desc']="Description must have more than 2 characters"
        if len(postDATA['location'])<3:
            errors['location']="Location must be have more than 2 characters"
        return errors
    
    def editValidator(self, postDATA):
        errors={}
        if len(postDATA['title'])<3:
            errors['title']="Title must have more than 2 characters"
        if len(postDATA['desc'])<3:
            errors['desc']="Description must have more than 2 characters"
        if len(postDATA['location'])<3:
            errors['location']="Location must be have more than 2 characters"
        return errors


class Job(models.Model):
    title = models.CharField(max_length=45)
    location = models.CharField(max_length=100)
    desc = models.TextField()
    category = models.TextField()
    creator = models.ForeignKey(User, related_name='jobs_created', on_delete=models.CASCADE)
    employee = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = jobManager()
    
