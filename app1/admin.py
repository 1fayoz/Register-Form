from django.contrib import admin
# from .models import Authors, Genres, Book, Books_authors
from .models import registration

# @admin.register(Authors)
# class AuthorAdmin (admin.ModelAdmin):
#     list_display = ('id', 'name', 'bio', )

# @admin.register(Genres)
# class GenresAdmin (admin.ModelAdmin):
#     list_display = ('id', 'name', 'discription', )

# @admin.register(Book)
# class BookAdmin (admin.ModelAdmin):
#     list_display = ('id', 'title', 'discription','genres_id', )


# @admin.register(Books_authors)
# class Books_authorsAdmin (admin.ModelAdmin):
#     list_display = ('id', 'book_id', 'author_id','is_main_author', )


# admin.site.register(Authors)
# admin.site.register(Genres)
# admin.site.register(Book)
# admin.site.register(Books_authors)

admin.site.register(registration)

 