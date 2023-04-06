# Simple-Django-CRUD
Simple application using the basics functions of CRUD. Utilizing Python framework Django.
Project based on tutorial from: <a href="https://www.thepythoncode.com/article/build-bookstore-app-with-django-backend-python">thepythoncode.com</a>

The process of building a book store application using Django:
- Started by creating a project (Creating a virtual enviorement, $pip install Django Pillow, $django-admin startproject bookstore)
- Then an application ($cd bookstore, $python manage.py startapp books, Have to add 'books' into INSTALLED_APPS)
- Add Model for book details (Create 'models.py' and implement the class 'Book')
- Created views to display (With functions in 'views.py', and paths in 'urls.py'):
	- Book Details
	- Add Book
	- Update Book
	- Delete Book
- Created URLs for book app (On 'views.py' file and put the urls for each def function)
- And tied every view to its respective URL (Create 'urls.py' and put the urlpatterns with django.urls path. Include in bookstore's url the books.urls)
