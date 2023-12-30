from django.contrib import admin

from example.models import Article, Author, Category

admin.site.register([Author, Article, Category])
