from django import forms
from .models import *


class fileform(forms.ModelForm):
    class Meta:
        model = project_info
        fields = '__all__'

        # fields = ('projectname', 'project_id', 'domain', 'file')
        labels={
            'projectname': '',
            'project_id': '',
            'domain': '',
            'file': '',
        }
        widgets={
            'projectname':forms.TextInput(attrs={'class':'input100','placeholder':"Project Name",}),
            'project_id':forms.TextInput(attrs={'class':'input100','placeholder':"Project ID"}),
            'domain':forms.TextInput(attrs={'class':'input100','placeholder':"Domain/Segment Name"}),
            'file':forms.FileInput(attrs={'class':'input100'}),
        }
