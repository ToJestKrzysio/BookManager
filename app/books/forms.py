from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, help_text="Search for books to import.")
