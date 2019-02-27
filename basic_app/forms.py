from django import forms

class Class_Form_1(forms.Form):
    mgtIP = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
