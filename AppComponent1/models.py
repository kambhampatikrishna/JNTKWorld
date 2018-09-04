from django.db import models

# Create your models here.
class Branches(models.Model):
    branchname=models.CharField(max_length=10,default='cse')
    regulation=models.CharField(max_length=10,default='r16')
    semester=models.CharField(max_length=10,default='1-1')
    subname = models.CharField(max_length=10)
    pdf = models.FileField(upload_to='pdf',blank=True)
    unit = models.CharField(max_length=100,default=1)
    teachername = models.CharField(max_length=100,default=None)
    clgname = models.CharField(max_length=100,default=None)
    views = models.IntegerField(default=0)
    #urls = models.URLField(max_length=300,blank=False,default='x')

    
    def __str__(self):
        return self.subname

class videourls(models.Model):
    TopicName = models.CharField(max_length=100)
    Topicpdf = models.FileField(upload_to='pdf',blank=True,null=True,default='x')
    Topicurl = models.URLField(blank=True,null=True)
    subname = models.CharField(max_length=100)
    views = models.IntegerField(default=0) 
    clgname = models.CharField(max_length=100,default=None)


    def __str__(self):
        return self.TopicName
    
    def get_resource(self):
        return self.Topicurl