from django.test import TestCase
from catalog.models import Author, Book, BookInstance, Genre, Language


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')


class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Genre.objects.create(name='Comedy')

    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_name_help_text(self):
        genre = Genre.objects.get(id=1)
        help_text = genre._meta.get_field('name').help_text
        self.assertEquals(help_text, 'Enter a book genre (e.g. Science Fiction, French Poetry etc.)')

    def test_object_name_is_genre_name(self):
        genre = Genre.objects.get(id=1)
        expected_genre_name = f'{genre.name}'
        self.assertEquals(expected_genre_name, str(genre))


class LanguageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Language.objects.create(name='Irish')

    def test_name_label(self):
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_name_help_text(self):
        language = Language.objects.get(id=1)
        help_text = language._meta.get_field('name').help_text
        self.assertEquals(help_text, "Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def test_object_name_is_language_name(self):
        language = Language.objects.get(id=1)
        expected_language_name = f'{language.name}'
        self.assertEquals(expected_language_name, str(language))


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(last_name='Duma', first_name='Alexandr')
        genre1 = Genre.objects.create(name='Romantic novel')
        genre2 = Genre.objects.create(name='Historical novel')
        genre_objects_for_book = Genre.objects.all()
        language = Language.objects.create(name='French')
        Book.objects.create(
            title='The Count of Monte Cristo',
            author=author,
            summary='A romantic novel about a prisoner of the castle If',
            isbn='9876543212345',
            #genre=test_genre,
            language=language,
        )
        Book.genre = genre_objects_for_book

    # Label tests
    def test_title_lable(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_author_lable(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label, 'ISBN')

    def test_genre_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEquals(field_label, 'genre')

    def test_language_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('language').verbose_name
        self.assertEquals(field_label, 'language')

    # Max Length tests
    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_summary_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEquals(max_length, 1000)

    def test_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEquals(max_length, 13)

    # Help Text test
    def test_summary_help_text(self):
        book = Book.objects.get(id=1)
        help_text = book._meta.get_field('summary').help_text
        self.assertEquals(help_text, 'Enter a brief description of the book')

    def test_isbn_help_text(self):
        book = Book.objects.get(id=1)
        help_text = book._meta.get_field('isbn').help_text
        self.assertEquals(help_text, '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    def test_genre_help_text(self):
        book = Book.objects.get(id=1)
        help_text = book._meta.get_field('genre').help_text
        self.assertEquals(help_text, 'Select a genre for this book')

    # Methods tests
    def test_object_name_is_book_title(self):
        book = Book.objects.get(id=1)
        expected_book_name = f'{book.title}'
        self.assertEquals(expected_book_name, str(book))

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(), '/catalog/book/1')

    def test_display_genre(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.display_genre(), 'Romantic novel, Historical novel')

    # Short description for Admin panel
    def test_display_genre_short_description(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.display_genre.short_description, 'Genre')


# Создать BookInstanceModelTest(TestCase)