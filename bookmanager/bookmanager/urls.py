"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

"""
1. The urlpatterns are fixed. Its value is the list.
2. The path entered in the browser is matched against each item in the urlpatterns in sequence
    If the match is successful, it leads directly to the appropriate module
    If the match is unsuccessful (every single one of the urlpatterns is matched), return 404.
3. The elements in urlpatterns are url
    The first parameter in the url is: regular expression
        r transferred meaning
        ^ A Strict Start
        $ A Strict End
4. What parts of the route entered in the browser are involved in regular matching?
    http://ip:port/path/?key=value
    The http://ip:port/ and get post parameters do not participate in regular matching.
5. If the match is successful with one of the current items, it leads to a sub-application to continue the match
    If the match is successful, stop the match and return to the corresponding view
    If the match is unsuccessful, it continues to match each item of the url in the following project until it matches each item
6. 
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('book/', include('book.urls'))
    url(r'^', include('book.urls')),
    url(r'^pay/', include('pay.urls'))
]
