from django import forms


not_allowed = ['rohitanand_', 'sumedha__05', 'reeteekaa_']


class getUsername(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), max_length=50, required=True)

