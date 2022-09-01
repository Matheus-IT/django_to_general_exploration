from django.shortcuts import render
from django.forms import modelformset_factory, inlineformset_factory
from example.forms import AuthorForm

from example.models import Author, Article


def home_view(request):
    model_form = AuthorForm(request.POST or None)

    InlineFormset = inlineformset_factory(
        Author, 
        Article, 
        form=AuthorForm,
        fields='__all__', 
        max_num=4, 
        extra=1, 
        can_delete=True
    )

    author = Author.objects.filter(name='author1').first()
    formset = InlineFormset(request.POST or None, instance=author)

    if formset.is_valid():
        formset.save()

    return render(request, 'example/home.html', {'formset': formset,
                                                 'model_form': model_form})
