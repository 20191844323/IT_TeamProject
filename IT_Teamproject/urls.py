"""
URL configuration for IT_Teamproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portal.views import LoginView, IndexView, RegisterView, RecipeView, SendVerificationCode

urlpatterns = [

    path("admin/", admin.site.urls),

    path('index/', IndexView),  # def视图写法

    path('login/', LoginView.as_view(), name='login'),  # 统一写类视图

    path('register/', RegisterView.as_view(), name='register'),

    path('validate_verification_code/', SendVerificationCode, name='validate-verification-code'),

    # 动态urls写recipes     path('recipes/<int:id>', RecipesView.as_view(),name='recipes')
    path('recipes/<int:recipe_id>/', RecipeView.as_view(), name='recipe_detail'),
]
