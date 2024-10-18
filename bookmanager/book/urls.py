from django.conf.urls import url
from book.views import index

urlpatterns = [
    # index/
    # The first argument to the url is: regular
    # The second argument to the url is: the name of the view function
    url(r'^index/$', index)
]