# Generated by Django 4.0.10 on 2023-10-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_alter_subscribers_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='title',
            field=models.TextField(blank=True, help_text='Job Title, if desired', max_length=50, null=True),
        ),
    ]
