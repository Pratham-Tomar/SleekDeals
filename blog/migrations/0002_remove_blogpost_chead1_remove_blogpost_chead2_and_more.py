# Generated by Django 5.0.6 on 2024-06-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='chead1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='chead2',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='head1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='head2',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Description',
            field=models.CharField(default='', max_length=100000),
        ),
    ]
