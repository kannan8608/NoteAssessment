from django.db import models

# Create your models here.


class Users(models.Model):
    user_name=models.CharField(max_length=50,blank=True,null=True)
    user_email=models.EmailField(blank=True,null=True)
    user_password=models.CharField(max_length=50,blank=True,null=True)
    last_update=models.DateTimeField(blank=True,null=True)
    create_on=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)


class Notes(models.Model):
    notes_title=models.CharField(max_length=300,blank=True,null=True)
    notes_content=models.TextField()
    create_on=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(blank=True,null=True)
    is_active=models.BooleanField(default=True)

