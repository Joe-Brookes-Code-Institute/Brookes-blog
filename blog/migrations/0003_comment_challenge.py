# Generated by Django 4.2.16 on 2024-09-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_post_content_post_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.FloatField(default=3.0),
        ),
    ]