from django.contrib import admin

from example.models import Article, Author

admin.site.register([Author, Article])
