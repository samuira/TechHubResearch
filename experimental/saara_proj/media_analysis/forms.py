from django import forms


class ImageAnalysisForm(forms.Form):
	file = forms.ImageField(required=True)
