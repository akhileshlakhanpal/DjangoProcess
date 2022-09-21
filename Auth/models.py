from django.db import models

class project_info(models.Model):
    projectname=models.CharField(max_length=100)
    project_id=models.CharField(max_length=20)
    domain=models.CharField(max_length=50)
    file=models.FileField(upload_to='file/',max_length=250,null=True,default=None)
    def __str__(self):
        return self.projectname
class project_details(models.Model):
    projectcode=models.CharField(max_length=100)
    methodplogy=models.CharField(max_length=100)
    geoscope=models.CharField(max_length=100)
    industry=models.CharField(max_length=100)
    pobjective=models.CharField(max_length=100)
    subjectsep=models.CharField(max_length=100)
    sme=models.CharField(max_length=100)
    raudience=models.CharField(max_length=100)
    analyst=models.CharField(max_length=100)
    dataanalyst=models.CharField(max_length=100)
    def __str__(self):
        return self.projectcode