"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
# from . import day1
from . import day2


# day1:
# urlpatterns = (
#     path('admin/', admin.site.urls),
#     path('', day1.index, name='index'),
#     path('navigator', day1.navigator, name='navigator'),
#     path('about', day1.about, name='about')
# )

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', day2.index, name='index'),
    # path('', day1.index, name='index'),
    # path('navigator', day1.navigator, name='navigator'),
    path('analyze', day2.analyze, name='analyze'),

    #day3
    # path('Capatalizefirst', day2.Capatalizefirst, name='capfirst'),
    # path('newlineremove', day2.newlineremove, name='newlineremove'),
    # path('spaceremove', day2.spaceremove, name='spaceremove'),
    # path('charcount', day2.charcount, name='charcount')

)
