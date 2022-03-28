from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, help_text="Most generic search", required=False)
    title = forms.CharField(max_length=300, label="Title", required=False)
    author = forms.CharField(max_length=100, label="Author", required=False)
    publisher = forms.CharField(max_length=100, label="Publisher", required=False)
    subject = forms.CharField(max_length=100, label="Subject", required=False)
    isbn = forms.CharField(max_length=100, label="ISBN number", required=False)
