from django.contrib import admin
from .models import Author, Genre, Language, Book, BookInstance

# Register your models here.
#admin.site.register(Book)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

#admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('display_title', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


# admin.site.register(Author)
# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

# Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)



# SUPERUSER l: professor, p: library2021
# Library Members: john_reader, johnpassword
# Library Staff: elsa, elsapassword