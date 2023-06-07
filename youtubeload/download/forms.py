from django import forms


class FindForm(forms.Form):
    link = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'size': 50}))