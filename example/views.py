from django.shortcuts import render
from django.forms import modelformset_factory, inlineformset_factory
from example.forms import AuthorForm

from example.models import Author, Article


def home_view(request):
    return render(request, 'example/home.html', {})
