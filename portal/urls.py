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

from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", Logout, name='logout'),
    path("", IndexView.as_view(), name='index'),
    path("myaccount/", MyAccount, name='myaccount'),
    path("comment/", Comments, name='comment'),
    path("sendmail/", SendMailView, name='sendmail'),
    path("register/", RegisterView.as_view(), name='register'),
    path("recipe/", RecipesView.as_view(), name='recipe'),
    path("forgotpassword/", ForgotPasswordView.as_view(), name='forgotpassword'),
    path("recipes/", RecipesView.as_view(), name='recipes'),
    path("publishrecipes/", PublishRecipes, name='publishrecipes'),
    path("contact_us/", ContactUsView.as_view(), name='contact_us'),
    path("search/", SearchView.as_view(), name='search'),
    path("information/", InformationView.as_view(), name='information'),
    path("myrecipes/",MyRecipesView.as_view(),name="myrecipes"),
    path("ingredients/",IngredientView.as_view(),name="ingredients"),
    path("likedrecipes/",LikedRecipesView.as_view(),name="likedrecipes"),
    path("allrecipes/",AllRecipesView.as_view(),name="allrecipes")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
