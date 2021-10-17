from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('authors', views.authors),
   path('createbook', views.createbook),
   # createauthor was done in the "authors" method, via an "if POST" statement
   path('books/<int:book_id>', views.book_info),
   path('authors/<int:auth_id>', views.author_info),
   path('addauthor/<int:book_id>', views.addauthor),
   path('addbook/<int:auth_id>', views.addbook)
]