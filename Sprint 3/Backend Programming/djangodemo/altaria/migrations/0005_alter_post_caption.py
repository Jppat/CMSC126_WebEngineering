# Generated by Django 3.2.4 on 2021-06-30 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('altaria', '0004_post_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(default='', max_length=200),
        ),
    ]