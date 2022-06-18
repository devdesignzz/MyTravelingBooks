from django.contrib import admin
from .models import Genre, BookReview, TrendingBook, PopularBook, Blog, Quote, WebsiteDetail

# Register your models here.

admin.site.register(Genre)
admin.site.register(BookReview)
admin.site.register(TrendingBook)
admin.site.register(PopularBook)
admin.site.register(Blog)
admin.site.register(Quote)
admin.site.register(WebsiteDetail)
