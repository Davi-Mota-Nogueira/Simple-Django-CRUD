from django.shortcuts import render, redirect
from .models import Book
from .forms import EditBookForm

# Create your views here.

# Listing all the books
def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/home.html', context)

# Listing only one book and your informations
def book_detail(request, id):
    book = Book.objects.get(pk=id)
    context = {'book':book}
    return render(request, 'books/book-detail.html', context)

# URL for adding books
def add_book(request):
    if (request.method == 'POST'):
        data = request.POST
        image = request.FILES.get('image-file')
        # Creating and saving the new object
        book = Book.objects.create(
            title = data['title'],
            author = data['author'],
            isbn = data['isbn'],
            price = data['price'],
            image = image
        )
        return redirect('home')
    # For other types of requests, like GET, will redirect to add-book page
    return render(request, 'books/add-book.html')

# Editing a book
def edit_book(request, id):
    book = Book.objects.get(pk=id)
    # Populating the form with the book informations
    form = EditBookForm(instance=book)
    if request.method == 'POST':
        form = EditBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'books/update-book.html', context)

# Delete a book, must have the id of the book
def delete_book(request, id):
    book = Book.objects.get(pk=id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    context = {'book':book}
    return render(request, 'books/delete-book.html', context)