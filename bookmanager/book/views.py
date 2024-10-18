from django.shortcuts import render
from book.models import BookInfo
from django.http import HttpRequest, HttpResponse

# Create your views here.
"""
View
1.It's a Python function.
2.The first parameter of the function is the request. It is an instance object of HttpRequest.
3.A response must be returned. It is an instance object / subclass instance object of HttpResponse.
"""

# def index(request):
#     name = 'Alex'
#     # Parameter 1: Current request
#     # Parameter 2: Template file
#     # Parameter 3: context Pass the parameter
#
#     context = {
#         'name': name
#     }
#     return render(request, 'index.html', context)

def index(request):
    # 1. Querying data into the database
    books = BookInfo.objects.all()
    # 2. Organizing data
    context = {
        'books': books
    }
    # 3. Passing to a template
    return render(request, 'index.html', context)
