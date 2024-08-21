from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)

    def  __str__(self):
        return f"{self.title} - {self.year}"


class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.TextField(max_length=200)
    birth_data = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_data = models.DateField()
    Publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")

    def __str__(self):
        return self.title
