from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Genre, BookReview, Blog, PopularBook, TrendingBook, Quote, WebsiteDetail
import operator
from functools import reduce
from django.db.models import Q

# Create your views here.

def index(request):

    genres = Genre.objects.all()[::-1]
    blogs = Blog.objects.all()[::-1]
    reviews = BookReview.objects.all()[::-1]
    popular_books = PopularBook.objects.all()[::-1]
    trending_books = TrendingBook.objects.all()
    quotes = Quote.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')
    
    if len(genres) >= 6:
        footer_genres = genres[:5]
    else:
        footer_genres = genres[:len(genres)]

    if len(blogs) >= 3:
        footer_blogs = blogs[:3]
    else:
        footer_blogs = blogs[:len(blogs)]

    if len(reviews) >= 6:
        footer_reviews = reviews[:5]
    else:
        footer_reviews = reviews[:len(reviews)]


    if len(popular_books) >= 8:
        popularBooks = popular_books[:8]
    else:
        popularBooks = popular_books[:len(popular_books)]

    return render(request, 'index.html', {"genres":genres, "footer_genres":footer_genres, "footer_blogs":footer_blogs,
    'quotes':quotes, "footer_reviews":footer_reviews, 'popularBooks':popularBooks, 'finalTrendingBooks': trending_books,
    'reviews':reviews, 'website':website})

# "genres":genres, "footer_genres":footer_genres, "footer_blogs":footer_blogs, "footer_reviews":footer_reviews

def contact(request):

    genres = Genre.objects.all()[::-1]
    blogs = Blog.objects.all()[::-1]
    reviews = BookReview.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')

    if len(genres) >= 6:
        footer_genres = genres[:5]
    else:
        footer_genres = genres[:len(genres)]

    if len(blogs) >= 3:
        footer_blogs = blogs[:3]
    else:
        footer_blogs = blogs[:len(blogs)]

    if len(reviews) >= 6:
        footer_reviews = reviews[:5]
    else:
        footer_reviews = reviews[:len(reviews)]


    if request.method == "GET":
        message_name = request.POST.get('your-name')

        return render(request, 'contact.html', {"message_name":message_name, "genres":genres, 'website':website, 
        "footer_genres":footer_genres, "footer_blogs":footer_blogs, "footer_reviews":footer_reviews})

    else:
        return render(request, 'contact.html', {"genres":genres, "footer_genres":footer_genres, 
        "footer_blogs":footer_blogs, "footer_reviews":footer_reviews})



def about(request):

    genres = Genre.objects.all()[::-1]
    blogs = Blog.objects.all()[::-1]
    reviews = BookReview.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')

    
    if len(genres) >= 6:
        footer_genres = genres[:5]
    else:
        footer_genres = genres[:len(genres)]

    if len(blogs) >= 3:
        footer_blogs = blogs[:3]
    else:
        footer_blogs = blogs[:len(blogs)]

    if len(reviews) >= 6:
        footer_reviews = reviews[:5]
    else:
        footer_reviews = reviews[:len(reviews)]


    return render(request, 'about.html', {"genres":genres, "footer_genres":footer_genres, 
    "footer_blogs":footer_blogs, "footer_reviews":footer_reviews, "website":website})



def reviews(request):

    genres = Genre.objects.all()[::-1]
    blogs = Blog.objects.all()[::-1]
    reviews = BookReview.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')

    if len(genres) >= 6:
        footer_genres = genres[:5]
    else:
        footer_genres = genres[:len(genres)]

    if len(blogs) >= 3:
        footer_blogs = blogs[:3]
    else:
        footer_blogs = blogs[:len(blogs)]

    if len(reviews) >= 6:
        footer_reviews = reviews[:5]
    else:
        footer_reviews = reviews[:len(reviews)]

    Books = BookReview.objects.all()[::-1]
    return render(request, 'reviews.html', {"Books":Books, "genres":genres, "footer_genres":footer_genres, 
    "footer_blogs":footer_blogs, "footer_reviews":footer_reviews, 'website':website})


def review(request, slug):

    genres = Genre.objects.all()[::-1]
    blogs = Blog.objects.all()[::-1]
    reviews = BookReview.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')

    if len(genres) >= 6:
        footer_genres = genres[:5]
    else:
        footer_genres = genres[:len(genres)]

    if len(blogs) >= 3:
        footer_blogs = blogs[:3]
    else:
        footer_blogs = blogs[:len(blogs)]

    if len(reviews) >= 6:
        footer_reviews = reviews[:5]
    else:
        footer_reviews = reviews[:len(reviews)]

    book = BookReview.objects.get(slug=slug)
    nextReview = BookReview.objects.filter(id__gt=book.id).order_by('id').first()
    prevReview = BookReview.objects.filter(id__lt=book.id).order_by('id').last()

    moreReviews  = BookReview.objects.all().order_by('?')[:6]

    if nextReview == None:
        nextBook = BookReview.objects.first()
    else:
        nextBook = nextReview

    if prevReview == None:
        prevBook = BookReview.objects.last()
    else:
        prevBook = prevReview

    return render(request, 'review.html', {'book':book, 'nextReview':nextBook,'previousReview':prevBook,
    "moreReviews":moreReviews, "genres":genres, "footer_genres":footer_genres, "footer_blogs":footer_blogs, 
    "footer_reviews":footer_reviews, 'website':website})



def genre(request, slug):

    genres = Genre.objects.all()[::-1]
    blogs = Blog.objects.all()[::-1]
    reviews = BookReview.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')

    if len(genres) >= 6:
        footer_genres = genres[:5]
    else:
        footer_genres = genres[:len(genres)]

    if len(blogs) >= 3:
        footer_blogs = blogs[:3]
    else:
        footer_blogs = blogs[:len(blogs)]

    if len(reviews) >= 6:
        footer_reviews = reviews[:5]
    else:
        footer_reviews = reviews[:len(reviews)]
    

    genre = Genre.objects.get(slug=slug)
    books = BookReview.objects.filter(genre_id=genre.id)
    return render(request, 'genre.html', {'genre':genre, 'books':books, "genres":genres, 'website':website,
    "footer_genres":footer_genres, "footer_blogs":footer_blogs, "footer_reviews":footer_reviews})


def blogs(request):
    
    genres = Genre.objects.all()[::-1]
    blogs = Blog.objects.all()[::-1]
    reviews = BookReview.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')

    if len(genres) >= 6:
        footer_genres = genres[:5]
    else:
        footer_genres = genres[:len(genres)]

    if len(blogs) >= 3:
        footer_blogs = blogs[:3]
    else:
        footer_blogs = blogs[:len(blogs)]

    if len(reviews) >= 6:
        footer_reviews = reviews[:5]
    else:
        footer_reviews = reviews[:len(reviews)]

    
    return render(request, 'blogs.html', {'blogs':blogs, "genres":genres, "footer_genres":footer_genres, 
    "footer_blogs":footer_blogs, "footer_reviews":footer_reviews, 'website':website})


def blog(request, slug):

    genres = Genre.objects.all()[::-1]
    blogs = Blog.objects.all()[::-1]
    reviews = BookReview.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')

    if len(genres) >= 6:
        footer_genres = genres[:5]
    else:
        footer_genres = genres[:len(genres)]

    if len(blogs) >= 3:
        footer_blogs = blogs[:3]
    else:
        footer_blogs = blogs[:len(blogs)]

    if len(reviews) >= 6:
        footer_reviews = reviews[:5]
    else:
        footer_reviews = reviews[:len(reviews)]

    blog = Blog.objects.get(slug=slug)
    nextBlogObj = Blog.objects.filter(id__gt=blog.id).order_by('id').first()
    prevBlogObj = Blog.objects.filter(id__lt=blog.id).order_by('id').last()

    if nextBlogObj == None:
        nextBlog = Blog.objects.first()
    else:
        nextBlog = nextBlogObj

    if prevBlogObj == None:
        prevBlog = Blog.objects.last()
    else:
        prevBlog = prevBlogObj

    return render(request, 'blog.html', {"blog":blog, 'nextBlog':nextBlog, 'prevBlog':prevBlog, 'website':website,
    "genres":genres, "footer_genres":footer_genres, "footer_blogs":footer_blogs, "footer_reviews":footer_reviews})


def search(request):
    
    genres = Genre.objects.all()[::-1]
    blogs = Blog.objects.all()[::-1]
    reviews = BookReview.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')

    if len(genres) >= 6:
        footer_genres = genres[:5]
    else:
        footer_genres = genres[:len(genres)]

    if len(blogs) >= 3:
        footer_blogs = blogs[:3]
    else:
        footer_blogs = blogs[:len(blogs)]

    if len(reviews) >= 6:
        footer_reviews = reviews[:5]
    else:
        footer_reviews = reviews[:len(reviews)]

    return render(request, 'search.html', {"genres":genres, "footer_genres":footer_genres, 
    "footer_blogs":footer_blogs, "footer_reviews":footer_reviews, 'website':website})

def search(request):

    query = request.GET.get("s")

    if query.strip() :
        split_query = query.strip().split(" ")
        Books = BookReview.objects.filter(reduce(operator.or_,
            (Q(name__icontains=x) | Q(author__icontains=x) for x in split_query)))
    else:
        Books = BookReview.objects.all()[::-1]

    genres = Genre.objects.all()[::-1]
    blogs = Blog.objects.all()[::-1]
    reviews = BookReview.objects.all()[::-1]
    website = WebsiteDetail.objects.get(linked_by='Website Details')

    if len(genres) >= 6:
        footer_genres = genres[:5]
    else:
        footer_genres = genres[:len(genres)]

    if len(blogs) >= 3:
        footer_blogs = blogs[:3]
    else:
        footer_blogs = blogs[:len(blogs)]

    if len(reviews) >= 6:
        footer_reviews = reviews[:5]
    else:
        footer_reviews = reviews[:len(reviews)]

    return render(request, 'search.html', {"Books":Books, "search_term": query,
        "genres":genres, "footer_genres":footer_genres,  "footer_blogs":footer_blogs,
        "footer_reviews":footer_reviews, 'website':website})