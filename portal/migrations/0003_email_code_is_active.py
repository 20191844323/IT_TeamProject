# Generated by Django 4.1.7 on 2024-03-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0002_email_code_alter_user_icon"),
    ]

    operations = [
        migrations.AddField(
            model_name="email_code",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="state"),
        ),
    ]
