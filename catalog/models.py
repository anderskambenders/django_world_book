from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Genre(models.Model):
    """
    Model for Books genre. Includes char field for genre name and string representation.
    """

    name = models.CharField(max_length=200,
                            help_text='Enter book`s genre',
                            verbose_name='Book`s genre')

    def __str__(self):
        return self.name


class Language(models.Model):
    """
    Book language model for app. Includes char field for lang and string representation.
    """

    name = models.CharField(max_length=20,
                            help_text='Enter language',
                            verbose_name='Book language')

    def __str__(self):
        return self.name


class Author(models.Model):
    """
    Model of book`s Author. Includes name, lastname, dates of birth and death. String representation is lastname.
    """
    first_name = models.CharField(max_length=100,
                                  help_text="Enter author`s name",
                                  verbose_name='Author`s name')
    last_name = models.CharField(max_length=100,
                                 help_text="Enter author`s lastname",
                                 verbose_name='Author`s lastname')
    date_of_birth = models.DateField(help_text='Enter birth date',
                                     verbose_name='Birthdate',
                                     null=True, blank=True)
    date_of_death = models.DateField(help_text='Enter death date',
                                     verbose_name='Death date',
                                     null=True, blank=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    """
    Model for book. Includes title, genre(1tM), lang(1tM), author(MtM), summary, isbn.
    Includes string representation by the title.
    """
    title = models.CharField(max_length=200,
                             help_text='Enter book name',
                             verbose_name='Book name')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
                              help_text='Choose genre',
                              verbose_name='Genre', null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE,
                                 help_text='Choose language of book',
                                 verbose_name='Book language', null=True)
    author = models.ManyToManyField('Author', help_text='Choose author',
                                    verbose_name='Author')
    summary = models.TextField(max_length=1000, help_text='Enter book summary', verbose_name='Summary')
    isbn = models.CharField(max_length=13, help_text='Min 13 symbols', verbose_name='Book ISBN')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns URL for access to book instance
        """
        return reverse('book-detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Author'


class Status(models.Model):
    """
    Model for book status
    """
    name = models.CharField(max_length=20,
                            help_text='Enter book status',
                            verbose_name='Book status')

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    """
    Model for book instance. Includes book (1tM), inv number
    """
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True,
                               help_text='Enter inventory number of book',
                               verbose_name='Inventory number')
    imprint = models.CharField(max_length=200,
                               help_text='Enter publishing and year',
                               verbose_name='Publishing house')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True,
                               help_text='Change status', verbose_name='Status of book example')
    due_back = models.DateField(null=True, blank=True,
                                help_text='Enter end of status term',
                                verbose_name='End of status term')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 verbose_name='Borrower',
                                 help_text='Choose book borrower'
                                 )
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        return f'{self.inv_nom} // {self.book}  // {self.status}'
