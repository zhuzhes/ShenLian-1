from django import forms

class Class_Form_1(forms.Form):
    routerip = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
