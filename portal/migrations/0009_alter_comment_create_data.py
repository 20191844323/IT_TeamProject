# Generated by Django 4.1.7 on 2024-03-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0008_comment_create_data_alter_recipe_r_imagefield"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="create_data",
            field=models.DateTimeField(auto_now_add=True, verbose_name="create date"),
        ),
    ]