from django.utils.text import slugify

import string
import random

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    
    return res 

def generate_slug(text):
    new_slug = slugify(text)
    from Main.models import BookReview
    if BookReview.objects.filter(slug = new_slug).filter():
        return generate_slug(text + generate_random_string(3))

    return new_slug

def generate_slug_genre(text):
    new_slug = slugify(text)
    from Main.models import Genre
    if Genre.objects.filter(slug = new_slug).filter():
        return generate_slug(text + generate_random_string(3))

    return new_slug



def generate_slug_blog(text):
    new_slug = slugify(text)
    from Main.models import Blog
    if Blog.objects.filter(slug = new_slug).filter():
        return generate_slug(text + generate_random_string(3))

    return new_slug