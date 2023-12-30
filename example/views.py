from django.shortcuts import render
from django.forms import modelformset_factory, inlineformset_factory
from example.forms import AuthorForm
from django.db.models import F, Func, IntegerField
from django.db.models.functions import ExtractYear, Now
from example.models import Author, Article, Category
import datetime

from example.utils import *


@how_many_queries
def home_view(request):
    result = Author.objects.annotate(
        age=ExtractYear(Now()) - ExtractYear('birth_date')
    ).filter(age__gt=20)
    print('\nfilter by age >>>', result)
    print()
    return render(request, 'example/home.html', {})
    