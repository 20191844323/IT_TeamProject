from django.db import models

# Create your models here.

'''
注册时候加验证码逻辑
缓存进行验证码生成 POST请求
'''

class User(models.Model):
    nickname = models.CharField(max_length=20, verbose_name="nickname")
    password = models.CharField(max_length=256,blank=True, null=True)
    email = models.EmailField(verbose_name="email",unique=True)
    # 或Binary
    icon = models.TextField(null=True)

    class Mate:
        verbose_name = "user information"
        verbose_name_plural = verbose_name
        db_table = "user"

class Manager(models.Model):
    nickname = models.CharField(max_length=20, verbose_name="nickname")
    password = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField(verbose_name="email", unique=True)

class Recipe(models.Model):
    title = models.CharField(max_length=50,verbose_name="title")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, verbose_name="category")
    avg_rating = models.FloatField(verbose_name="avg_rating")  #前端控制输出精度
    content = models.TextField(verbose_name="content")
    r_imagefield = models.TextField()

class Comment(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(verbose_name="rating",default=0)

class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)






