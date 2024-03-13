from django.shortcuts import HttpResponse
from django.views.generic.base import View
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.db.models import Avg

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import mail
from .models import *
from django.contrib import messages
from datetime import datetime, timedelta
from django.contrib.messages import constants as message_constants
import base64
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO


# 发送邮箱
def email_(email):
    a = random.randint(111111, 999999)
    mail.send_mail(
        subject='验证码',
        message=f'   尊敬的用户，您的验证码是 \n\n \t{a}\t \n\n该验证码有效时间是 10 min，请在有效时间内使用！',
        # 必须是发送的邮箱号
        from_email='2680059542@qq.com',
        recipient_list=[email]
    )
    return a

# 验证登入装饰器
def chack_login(fn):
    def wrap(request, *args, **kwargs):
        if 'nickname' not in request.session and 'id' not in request.session:
            username = request.COOKIES.get('nickname')
            Id = request.COOKIES.get('id')
            if username and Id:
                request.session['nickname'] = username
                request.session['id'] = Id
            else:
                return HttpResponseRedirect(reverse('login'))
        return fn(request, *args, **kwargs)
    return wrap

# 首页
class IndexView(View):
    def get(self, request, *args, **kwargs):
        # 返回首页数据
        # 获取收藏个数
        dict_ = {}
        count_favorite = 0
        if 'nickname' in request.session and 'id' in request.session:
            count_favorite = get_favorites(request.session['id'])
        recipes = Recipe.objects.annotate(avg__rating=Avg('comment__rating'))
        # 对食谱进行降序排序并提取前五名
        top_three = recipes.order_by('-avg__rating')[:5]
        dict_["count_favorite"] = count_favorite
        dict_["top_three"] = top_three
        return render(request, "index.html", dict_)

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is a POST response')

# 登录
class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.session.get('id') and request.session.get('nickname'):
            return HttpResponseRedirect(reverse("index"))
        nickname = request.COOKIES.get('nickname')
        Id = request.COOKIES.get('id')
        if nickname and Id:
            request.session['nickname'] = nickname
            request.session['id'] = Id
            return HttpResponseRedirect(reverse("index"))
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email)
        if password == user.password:
            # 登录保持
            request.session['id'] = user.id
            request.session['nickname'] = user.nickname
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "密码或用户名错误！")
            return HttpResponseRedirect(reverse("login"))

# 退出登入,返回首页
@chack_login
def Logout(request):
    # 删除 session
    if 'nickname' in request.session:
        del request.session['nickname']
    if 'id' in request.session:
        del request.session['id']
    resp = HttpResponseRedirect(reverse("index"))
    # 删除 COOKIES
    if 'nickname' in request.COOKIES:
        resp.delete_cookie('nickname')
    if 'id' in request.COOKIES:
        resp.delete_cookie('id')
    return resp

class AllRecipesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "all_recipes.html")
# 注册
class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "register.html")

    def post(self, request, *args, **kwargs):
        # 在这里处理用户提交的注册信息
        # 例如，您可以从request.POST中获取用户名和密码，然后创建一个新的用户
        if request.method == 'POST':
            # 从 POST 请求中获取表单数据
            nickname = request.POST.get('nickname')
            password = request.POST.get('password')
            email = request.POST.get('email')
            email_code = Email_code.objects.get(email=email, is_active=1)
            code = email_code.code
            expiration_data = email_code.expiration_data
            if datetime.now() <= expiration_data.replace(tzinfo=None) and code == email_code.code:
                # 创建一个新的 User 对象
                user = User(nickname=nickname, password=password, email=email)
                # 将 User 对象保存到数据库
                user.save()
                # 验证码失效
                email_code.is_active = 0
                email_code.save()
            else:
                messages.error(request, "验证码错误或已过期")
                return HttpResponseRedirect(reverse("register"))
        messages.add_message(request, message_constants.SUCCESS, "注册成功，请登录")
        return HttpResponseRedirect(reverse("login"))

# 发送邮件
@csrf_exempt
def SendMailView(request):
    email = request.POST.get('email')
    data_new = datetime.now()
    ten_minutes_later = data_new + timedelta(minutes=10)
    try:
        aa = Email_code.objects.get(email=email, is_active=1)
        if aa:
            aa.is_active = 0
            aa.save()
    except:
        pass
    code = email_(email)
    data = {"code": code, "messages": "The email has been sent"}
    cmail_code = Email_code(email=email, code=code, expiration_data=ten_minutes_later)
    cmail_code.save()
    return JsonResponse(data)

# 个人信息
@chack_login
def MyAccount(request):
    dict_ = {}
    user_xx = User.objects.get(id=request.session.get('id'))
    dict_["user_xx"] = user_xx
    recipes_by_user = Recipe.objects.filter(user_id_id=request.session.get('id'))
    recipes_with_avg_ratings = (recipes_by_user.annotate(avg_rating=Avg('comment__rating'))
                                .values('id', 'title', 'user_id_id', 'content', 'r_imagefield', 'avg_rating'))
    dict_["recipes"] = recipes_with_avg_ratings
    return render(request, "user_center.html", dict_)

# 我发布了哪些食谱
class MyRecipesView(View):
    def get(self, request, *args, **kwargs):
        dict_ = {}
        user_xx = User.objects.get(id=request.session.get('id'))
        dict_["user_xx"] = user_xx
        recipes_by_user = Recipe.objects.filter(user_id_id=request.session.get('id'))
        recipes_with_avg_ratings = (recipes_by_user.annotate(avg_rating=Avg('comment__rating'))
                                    .values('id', 'title', 'user_id_id', 'content', 'r_imagefield', 'avg_rating'))
        dict_["recipes"] = recipes_with_avg_ratings
        return render(request, "my_recipes.html", dict_)


# 我喜欢哪些食谱
class LikedRecipesView(View):
    def get(self, request, *args, **kwargs):
        dict_ = {}
        user_xx = User.objects.get(id=request.session.get('id'))
        dict_["user_xx"] = user_xx
        recipes_by_user = Recipe.objects.filter(user_id_id=request.session.get('id'))
        recipes_with_avg_ratings = (recipes_by_user.annotate(avg_rating=Avg('comment__rating'))
                                    .values('id', 'title', 'user_id_id', 'content', 'r_imagefield', 'avg_rating'))
        dict_["recipes"] = recipes_with_avg_ratings
        return render(request, "liked_recipes.html", dict_)



# 个人信息界面
class InformationView(View):
    def get(self, request, *args, **kwargs):
        dict_ = {}
        user_xx = User.objects.get(id=request.session.get('id'))
        dict_["user_xx"] = user_xx
        return render(request, 'information.html',dict_)

class IngredientView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'ingredient.html')

# 食谱
class RecipesView(View):
    def get(self, request, *args, **kwargs):
        dict_ = {}
        recipe_id = request.GET.get('recipe_id')
        recipe = Recipe.objects.get(id=recipe_id)
        comments = Comment.objects.filter(recipe_id_id=recipe_id)
        recipes = Recipe.objects.annotate(avg__rating=Avg('comment__rating'))
        top_three = recipes.order_by('-avg__rating')[:3]
        dict_["recipe"] = recipe
        average_rating = Comment.objects.filter(recipe_id_id=recipe_id).aggregate(Avg('rating'))['rating__avg']
        dict_["comments"] = comments
        dict_["average_rating"] = average_rating
        dict_["top_three"] = top_three
        return render(request, 'recipes.html', dict_)

# 发布食谱
@chack_login
def PublishRecipes(request):
    if request.method == 'GET':
        dict_ = {}
        user_xx = User.objects.get(id=request.session.get('id'))
        dict_["user_xx"] = user_xx
        return render(request, 'publish_recipes.html', dict_)
    if request.method == 'POST':
        data = request.POST
        title = data['title']
        user_id = User.objects.get(id=request.session.get('id'))
        content = data['content']
        r_imagefield = data['path']
        r_imagefield_name = data['picpath']
        base64_data = r_imagefield.split(',')[1]
        decoded_data = base64.b64decode(base64_data)
        image_io = BytesIO(decoded_data)
        image_file = InMemoryUploadedFile(
            image_io,
            None,  # field_name is not required for InMemoryUploadedFile
            r_imagefield_name,  # 你可以设置你想要的文件名
            'image/jpeg',  # MIME type
            len(decoded_data),  # 文件大小
            None  # charset is not required for InMemoryUploadedFile
        )
        recipe = Recipe(title=title, content=content, user_id=user_id, r_imagefield=image_file)
        recipe.save()
        return HttpResponseRedirect(reverse("myaccount"))

# 联系我们
class ContactUsView(View):
    def get(self, request, *args, **kwargs):
        # 获取收藏个数
        try:
            favorites_sum = get_favorites(request.session.get('id'))
            # 登录了
            return render(request, "contact_us.html", {"favorites_sum": favorites_sum})
        except:
            # 没登录
            return render(request, "contact_us.html")

# 获取收藏个数
def get_favorites(Id):
    try:
        count = Favorite.objects.filter(user_id=Id).count()
        return count
    except:
        return 0

# 搜索
class SearchView(View):
    def get(self, request, *args, **kwargs):
        dict_ = {}
        try:
            favorites_sum = get_favorites(request.session.get('id'))
        except:
            favorites_sum = 0
        search = request.GET.get("search")
        dict_["search"] = search
        dict_["count_favorite"] = favorites_sum
        search_all = Recipe.objects.filter(title__icontains=search)
        dict_["search_all"] = search_all
        return render(request, "search.html", dict_)

# 评论
@chack_login
def Comments(request):
    recipe = Recipe.objects.get(id=request.POST.get('recipe_id'))
    try:
        if request.method == 'POST':
            user = User.objects.get(id=request.session.get('id'))
            rating = request.POST.get('rating')
            comment = request.POST.get('comment')
            comment_ = Comment(recipe_id=recipe, user_id=user, rating=rating, comment=comment)
            comment_.save()
            return HttpResponseRedirect('/recipe/?recipe_id=' + str(recipe.id))
    except:
        return HttpResponseRedirect('/recipe/?recipe_id=' + str(recipe.id))

# 忘记密码
class ForgotPasswordView(View):
    def post(self, request, *args, **kwargs):
        pass

# class RecipeView(View):
#     def get(self, request, *args, **kwargs):
#         recipe_id = kwargs.get('recipe_id')
#         print(f"Received recipe_id: {recipe_id}")
#
#         recipe = get_object_or_404(Recipe, pk=recipe_id)
#         print(f"Found recipe: {recipe}")
#
#         return render(request, 'recipes.html', {'recipe': recipe})
#
#     def post(self, request, *args, **kwargs):
#         return HttpResponse('This is a POST response from RecipeView')
#
#     def top_three_recipes(self, request):
#         # 计算每个食谱的平均评分
#         recipes = Recipe.objects.annotate(avg_rating=Avg('comment__rating'))
#         # 对食谱进行降序排序并提取前三名
#         top_three = recipes.order_by('-avg_rating')[:3]
#         # 将 top_three 传递，或者以其他方式处理
#         return top_three
#
#
# class ContactUsView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "contact_us.html")
#
#
# class UserCenterView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "user_center.html")
#
#
# class InformationView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "information.html")
#
#
# class MyRecipesView(View):
#     def get(self, request, *args, **kwargs):
#         def user_view(request):
#             users = User.objects.all()
#         return render(request, "my_recipes.html")
#
#
# class PublishRecipesView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "publish_recipes.html")
#
#     def submit_recipie(self, request):
#         if request.method == 'POST':
#             user = User.objects.get(username='username')
#             title = request.POST['title']
#             content = request.POST['content']
#             image = request.FILES['picpath']
#                 # 处理图片上传...
#                 # 创建一个新的 Recipe 对象
#             recipe = Recipe(title=title, user_id=user.id, category= 0, avg_rating= 0, content=content, r_imagefield=image)
#                 # 将 Recipe 对象保存到数据库
#             recipe.save()
#
#
# @require_POST
# @csrf_exempt
# def SendVerificationCode(request):
#     email = request.POST.get('email')
#
#     if not email:
#         return JsonResponse({'error': 'Email is required.'}, status=400)
#
#     verification_code = ''.join(random.choices('0123456789', k=4))
#
#     # 发送邮件
#     send_mail(
#         'Verification Code',
#         f'Your verification code is: {verification_code}',
#         'your_email@example.com',  # 发件邮箱
#         [email],
#         fail_silently=False,
#     )
#
#     return JsonResponse({'success': True})
#
#
# class SearchRecipesView(View):
#     @require_http_methods(["GET", "POST"])
#     def get(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             query = request.POST.get('q', '')  # 获取POST参数
#             results = Recipe.objects.filter(my_field__icontains=query)  # 执行搜索
#             if results.exists():  # 检查结果集是否为空
#                 return render(request, 'search.html', {'results': results})  # 如果不为空，渲染模板
#             else:
#                 return render(request, 'search.html', {'message': 'No results found.'})  # 如果为空，返回一个消息
#         else:
#             return render(request, 'search.html')

