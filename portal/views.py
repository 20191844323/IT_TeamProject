from django.shortcuts import render,HttpResponse,redirect
from .models import Recipe
from django.views.generic.base import View

# Create your views here.

def IndexView(request):
    return render(request, "index.html")

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is a POST response')

'''
class RecipeView(View):
    def get(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(pk=recipe_id) 
        return render(request, 'recipe_detail.html', {'recipe': recipe})
        
后台
'''




