from django.db import models

class secondaryT_details(models.Model):
    projectcode=models.CharField(max_length=100)
    question_label=models.CharField(max_length=100)
    quantative_ans=models.CharField(max_length=100)
    qualitative_ans=models.CharField(max_length=100)
    text_input=models.CharField(max_length=100)

    def __str__(self):
        return self.projectcode