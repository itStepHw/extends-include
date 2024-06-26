# Generated by Django 4.2.13 on 2024-05-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cw', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': ('Категория',), 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['id'], 'verbose_name': ('Комментарий',), 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id'], 'verbose_name': ('Пост',), 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=255),
        ),
    ]
