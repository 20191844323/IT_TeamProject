from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Recipe
from django.views.generic.base import View
import random
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# Create your views here.

def IndexView(request):
    return render(request, "index.html")


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is a POST response')


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "register.html")

    def post(self, request, *args, **kwargs):
        # 在这里处理用户提交的注册信息
        # 例如，您可以从request.POST中获取用户名和密码，然后创建一个新的用户
        return HttpResponse('This is a POST response from RegisterView')


class RecipeView(View):
    def get(self, request, *args, **kwargs):
        recipe_id = kwargs.get('recipe_id')
        print(f"Received recipe_id: {recipe_id}")

        recipe = get_object_or_404(Recipe, pk=recipe_id)
        print(f"Found recipe: {recipe}")

        return render(request, 'recipes.html', {'recipe': recipe})

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is a POST response from RecipeView')






@require_POST
@csrf_exempt
def SendVerificationCode(request):
    email = request.POST.get('email')

    if not email:
        return JsonResponse({'error': 'Email is required.'}, status=400)

    verification_code = ''.join(random.choices('0123456789', k=4))

    # 发送邮件
    send_mail(
        'Verification Code',
        f'Your verification code is: {verification_code}',
        'your_email@example.com',  # 发件邮箱
        [email],
        fail_silently=False,
    )

    return JsonResponse({'success': True})


'''
class RecipeView(View):
    def get(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(pk=recipe_id) 
        return render(request, 'recipe_detail.html', {'recipe': recipe})

后台
'''
