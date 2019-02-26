from django import forms

class Class_Form_1(forms.Form):
    SystemID = forms.CharField()
    LicenseLevel = forms.CharField()
    # uptime = forms.CharField()
    # version = forms.CharField()
    # free-memory = forms.CharField()
    # total-memory = forms.CharField()
    # cpu = forms.CharField()
    # cpu-frequency = forms.CharField()
    # architecture-name = forms.CharField()
    # board-name = forms.CharField()
