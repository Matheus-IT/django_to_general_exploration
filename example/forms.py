from django import forms
from .models import Article, Author


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
