from django import forms

class GrammerCheck(forms.Form):
    TextArea = forms.CharField(widget=forms.Textarea())
