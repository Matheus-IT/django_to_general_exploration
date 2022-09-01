from django.shortcuts import render
from django.forms import modelformset_factory, inlineformset_factory

from example.models import Author, Article


def home_view(request):
    InlineFormset = inlineformset_factory(
        Author, 
        Article, 
        fields='__all__', 
        max_num=4, 
        extra=1, 
        can_delete=True
    )
    author = Author.objects.filter().first()

    model_formset = InlineFormset(request.POST or None, instance=author)

    if model_formset.is_valid():
        model_formset.save()

    return render(request, 'example/home.html', {'formset': model_formset})
