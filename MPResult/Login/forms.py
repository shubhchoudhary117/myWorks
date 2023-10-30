from django import forms


class LoginFields(forms.Form):
    RollNo=forms.CharField(widget=forms.TextInput(attrs={'id':'roll','placeholder':'Roll Number'}))
    ApplicationId=forms.CharField(widget=forms.TextInput(attrs={'id':'application','placeholder':'Enter Valid No'}))

    