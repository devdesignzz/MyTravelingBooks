from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about-me', views.about, name='about'),
    path('book-reviews', views.reviews, name='reviews'),
    path('book-review/<slug:slug>', views.review, name='review'),
    path('book-review/genre/<slug:slug>', views.genre, name='genre'),
    path('blogs', views.blogs, name='blogs'),
    path('blog/<slug:slug>', views.blog, name='blog'),
    path('search-page', views.search, name='search')
]
