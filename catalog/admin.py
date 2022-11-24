from django.contrib import admin
from .models import Author, Genre, Book,Language, Bookinstance
from django.utils.translation import gettext_lazy as _

admin.site.site_header = ("Local Library Admin Site")
admin.site.site_title = ("Local Library Portal")
admin.site.index_title = ("Welcome to Local Library Admin Portal")


# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(Language)
# admin.site.register(Bookinstance)

#decorador para registrar el modelo
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','display_genre')
    list_filter = ('language','genre')
    search_fields = ('title',
            'author__first_name',
            'author__last_name')

# Register the Admin classes for BookInstance using the decorator
@admin.register(Bookinstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status_color','img_image')
    list_filter = ('status','due_back')
    search_fields = ('book__title',
            'book__author__first_name',
            'book__author__last_name')
    

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
