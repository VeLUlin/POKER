from django import forms

class Calculate(forms.Form):
	"""docstring for Calculate"""
	compression = forms.IntegerField(label='圧縮率')
	balance = forms.IntegerField(label='収支')