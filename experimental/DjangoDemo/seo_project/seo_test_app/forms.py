from django import forms


class DLForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    type = forms.CharField(max_length=255)