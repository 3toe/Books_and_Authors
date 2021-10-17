from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
   context = {
      "Booklist" : Book.objects.all()
   }
   return render(request, "index.html", context)

def createbook(request):
   if request.POST['title'] == "" or request.POST['desc'] == "":
      return redirect('/')
   Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
   return redirect('/')

def authors(request):
   if request.method == 'GET':
      context = {
         "Authorlist" : Author.objects.all()
      }
      return render(request, 'authors.html', context)
   if request.method == 'POST':
      if request.POST['firstname'] == "" or request.POST['lastname'] == "":
         return redirect('/authors')
      Author.objects.create(fname = request.POST['firstname'], lname = request.POST['lastname'], notes = request.POST['notes'])
      return redirect('/authors')

def addauthor(request, book_id):
   if request.POST['sel_author'] == "":
      return redirect('/')
   Author.objects.get(id=request.POST['sel_author']).books.add(Book.objects.get(id=book_id))
   return redirect('/')

def book_info(request, book_id): 
   context = {
      'book' : Book.objects.get(id=book_id),
      'Authorlist' : Author.objects.all(),
      'AvailList' : Author.objects.exclude(books=book_id)
   }
   return render(request, 'books.html', context)

def author_info(request, auth_id): 
   context = {
      'author' : Author.objects.get(id=auth_id),
      'Booklist' :Book.objects.all(),
      'AvailList' : Book.objects.exclude(authors=auth_id)
   }
   return render(request, 'authorinfo.html', context)

def addbook(request, auth_id):
   if request.POST['sel_book'] == "":
      return redirect('/')
   Book.objects.get(id=request.POST['sel_book']).authors.add(Author.objects.get(id=auth_id))
   return redirect('/authors')