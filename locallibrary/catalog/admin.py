from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(BookInstance)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


class BooksInline(admin.StackedInline):
    model = Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


admin.site.register(Genre)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('imprint', 'status', 'due_back', 'id')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )