# Generated by Django 4.1.1 on 2022-09-07 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter author`s name', max_length=100, verbose_name='Author`s name')),
                ('last_name', models.CharField(help_text='Enter author`s lastname', max_length=100, verbose_name='Author`s lastname')),
                ('date_of_birth', models.DateField(blank=True, help_text='Enter birth date', null=True, verbose_name='Birthdate')),
                ('date_of_death', models.DateField(blank=True, help_text='Enter death date', null=True, verbose_name='Death date')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter book name', max_length=200, verbose_name='Book name')),
                ('summary', models.TextField(help_text='Enter book summary', max_length=1000, verbose_name='Summary')),
                ('isbn', models.CharField(help_text='Min 13 symbols', max_length=13, verbose_name='Book ISBN')),
                ('author', models.ManyToManyField(help_text='Choose author', null=True, to='catalog.author', verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter book`s genre', max_length=200, verbose_name='Book`s genre')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter language', max_length=20, verbose_name='Book language')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter book status', max_length=20, verbose_name='Book status')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_nom', models.CharField(help_text='Enter inventory number of book', max_length=20, null=True, verbose_name='Inventory number')),
                ('imprint', models.CharField(help_text='Enter publishing and year', max_length=200, verbose_name='Publishing house')),
                ('due_back', models.DateField(blank=True, help_text='Enter end of status term', null=True, verbose_name='End of status term')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
                ('status', models.ForeignKey(help_text='Change status', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Status of book example')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Choose genre', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.genre', verbose_name='Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Choose language of book', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language', verbose_name='Book language'),
        ),
    ]