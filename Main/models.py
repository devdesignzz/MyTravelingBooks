from django.db import models
from froala_editor.fields import FroalaField
from .helpers import *

# Create your models here.

class Genre(models.Model):

    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='pics/genres')

    slug = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = generate_slug_genre(self.name)
        super(Genre, self).save(*args, **kwargs)



star_choice =(
    ("8", "Half Star Rating"),
    ("15", "One Star Rating"),
    ("29", "One and Half Star Rating"),
    ("40", "Two Star Rating"),
    ("48", "Two and Half Star Rating"),
    ("60", "Three Star Rating"),
    ("68.25", "Three and Half Star Rating"),
    ("80", "Four Star Rating"),
    ("88", "Four and Half Star Rating"),
    ("100", "Five Star Rating"),
    )

class BookReview(models.Model):
    
    name = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    rating = models.CharField(max_length=150, choices=star_choice)
    photo = models.ImageField(upload_to='pics/book-review')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    review = FroalaField()
    categories = models.CharField(max_length=500)
    Tags = models.CharField(max_length=200)
    instagram = models.CharField(max_length=500, null=True, blank=True)
    facebook  = models.CharField(max_length=500, null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    
    slug = models.SlugField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name + " | " + self.author


    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(BookReview, self).save(*args, **kwargs)



class TrendingBook(models.Model):
    book = models.ForeignKey(BookReview, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.book.name + " | " + self.book.author


class PopularBook(models.Model):
    book = models.ForeignKey(BookReview, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.name + " | " + self.book.author


class Blog(models.Model):

    Title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics/blog')
    category = models.CharField(max_length=200)
    Content = FroalaField()
    Date = models.DateField()

    slug = models.SlugField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.Title


    def save(self, *args, **kwargs):
        self.slug = generate_slug_blog(self.Title)
        super(Blog, self).save(*args, **kwargs)


class Quote(models.Model):
    title = models.CharField(max_length=200)
    quote = models.TextField()
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title + " | " + self.author


class WebsiteDetail(models.Model):

    Banner_upper_tagline = models.CharField(max_length=200)
    Banner_lower_tagline = models.CharField(max_length=200)
    Banner_first_line = models.CharField(max_length=50)
    Banner_second_line = models.CharField(max_length=50)

    About_Me_heading_paragraph = models.TextField()
    banner_image = models.ImageField(upload_to='pics/about')
    About_me = FroalaField()

    Footer_bio = models.TextField()
    Instagram_link = models.CharField(blank=True, null=True, max_length=200)
    Facebook_link = models.CharField(blank=True, null=True, max_length=200)
    Twitter_link = models.CharField(blank=True, null=True, max_length=200)
    Pinterest_link = models.CharField(blank=True, null=True, max_length=200)

    linked_by = models.CharField(max_length=15)

    def __str__(self):
        return self.linked_by + " | Do not add delete this or add any more" 