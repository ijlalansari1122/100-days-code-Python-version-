from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Borrower(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=200)
    due_date = models.DateField()
