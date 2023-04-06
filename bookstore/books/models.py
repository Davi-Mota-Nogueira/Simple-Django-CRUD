from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.CharField(max_length=100)
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # String representation to display after querying a book/books
    def __str__(self):
        return f'{self.title}'
    
    # Ordering the books by created date
    class Meta:
        ordering = ['-created_at']