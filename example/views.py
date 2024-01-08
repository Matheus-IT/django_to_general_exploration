from django.shortcuts import render
from django.forms import modelformset_factory, inlineformset_factory
from example.forms import AuthorForm
from django.db.models import F, Func, IntegerField, Q
from django.db.models.functions import ExtractYear, Now
from django.db.transaction import atomic
from example.models import Author, Article, Category
import datetime

from example.utils import *


@how_many_queries
def home_view(request):
    # Filtering by age using annotate
    # result = Author.objects.annotate(
    #     age=ExtractYear(Now()) - ExtractYear('birth_date')
    # ).filter(age__gt=20)

    # Using Q with and "&", and not "~"
    # result = Author.objects.filter(
    #     Q(name__startswith='Larry') & ~Q(name__startswith='Robert')
    # )

    # Making block of code atomic within a transaction
    with atomic():
        result = Author.objects.first()
        result.name = 'test'
        result.save()

        result.birth_date = '2000/12/1'
        result.save()

    # print('\nresult >>>', result)
    # print('\nsql query >>>', result.query)

    return render(request, 'example/home.html', {})
    