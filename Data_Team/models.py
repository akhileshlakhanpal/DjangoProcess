from django.db import models

class dataT_details(models.Model):
    projectcode=models.CharField(max_length=100)
    question_label=models.CharField(max_length=100)
    option_ans=models.CharField(max_length=100)
    text_input = models.CharField(max_length=100)

    def __str__(self):
        return self.projectcode
class data_result(models.Model):
    projectcode=models.CharField(max_length=100)
    file=models.FileField(max_length=100)

    def __str__(self):
        return self.projectcode