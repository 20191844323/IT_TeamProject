from django.db import models


# Create your models here.

class Email_code(models.Model):
    email = models.EmailField(verbose_name="email", unique=True)
    code = models.CharField(max_length=6, verbose_name="code")
    create_data = models.DateTimeField('create date', auto_now_add=True)
    expiration_data = models.DateTimeField('expiration date')
    is_active = models.BooleanField('state', default=True)

    class Mate:
        verbose_name = "email code"
        verbose_name_plural = verbose_name
        db_table = "email"


class User(models.Model):
    nickname = models.CharField(max_length=20, verbose_name="nickname")
    password = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField(verbose_name="email", unique=True)
    icon = models.FileField('icon', upload_to='image', default='image/1.jpg')

    class Mate:
        verbose_name = "user information"
        verbose_name_plural = verbose_name
        db_table = "user"

class Recipe(models.Model):
    title = models.CharField(max_length=50, verbose_name="title")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="content")
    r_imagefield = models.FileField('imagefield', upload_to='field', default='field/11.jpg')

    class Mate:
        verbose_name = "recipe"
        verbose_name_plural = verbose_name
        db_table = "recipe"

class Comment(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(verbose_name="rating", default=0)
    create_data = models.DateTimeField('create date', auto_now_add=True)

    class Mate:
        verbose_name = "comment"
        verbose_name_plural = verbose_name
        db_table = "comment"

class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Mate:
        verbose_name = "user favorite"
        verbose_name_plural = verbose_name
        db_table = "favorite"
