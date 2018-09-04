from django import forms
import account.forms

class SignupForm(account.forms.SignupForm):
    College_Name = forms.CharField(max_length=256)