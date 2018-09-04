from django import forms
from . import models

class postForm(forms.ModelForm):
    class Meta:
        model = models.Branches
        fields = ['branchname','regulation','semester','pdf','subname','unit']

class StudentpostForm(forms.ModelForm):
    class Meta:
        model = models.Branches
        fields = ['branchname','regulation','semester','subname','unit']     

class urlForm(forms.ModelForm):
    class Meta:
        model = models.videourls
        fields = ['TopicName','Topicpdf','Topicurl','subname']           