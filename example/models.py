from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
