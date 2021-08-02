
from django.urls import path,include
from collections import namedtuple
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('goadd/',views.goadd,name="goadd"),
    path('add/',views.add,name="add"),
    path('display/',views.display,name="display"),
    path('update/<int:id>',views.update,name="update"),
    path('updated/',views.updated,name="updated"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('splace/',views.splace,name="splace"),
    path('searchpla/',views.searchpla,name="searchpla"),
    path('sgen/',views.sgen,name="sgen"),
    path('searchgen/',views.searchgen,name="searchgen"),
    path('cvoter/',views.cvoter,name="cvoter"),
]
