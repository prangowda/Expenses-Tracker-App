from django.db import models

class BookCategory(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publishing_date = models.DateField()
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    distribution_expenses = models.DecimalField(max_digits=10, decimal_places=2)


# db models.
