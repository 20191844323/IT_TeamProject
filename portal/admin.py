from django.contrib import admin
from .models import *

# Register your models here.
# 设置header
admin.site.site_header = 'Management backend'
# 设置title
admin.site.site_title = 'Management backend'
admin.site.index_title = 'Management backend'


@admin.register(Email_code)
class Email_codeAdmin(admin.ModelAdmin):
    list_display = ['email', 'code', 'create_data', 'expiration_data', 'is_active']
    # 在数据新增或修改的页面设置可编辑的字段
    fields = ['email', 'code', 'expiration_data']
    list_per_page = 100
    search_fields = ['email']
    ordering = ['-create_data']
    sortable_by = ['create_data', 'expiration_data']
    list_filter = ['email']
    # 设置“动作”栏的位置
    actions_on_top = False
    actions_on_bottom = False
    list_display_links = ['email']
    # 可见不可修改
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['email', 'code', 'create_data', 'expiration_data', 'is_active']
        else:
            return []

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'password', 'email', 'icon']
    # 在数据新增或修改的页面设置可看见的字段
    fields = ['nickname', 'email', 'password', 'icon']
    list_per_page = 100
    search_fields = ['nickname']
    list_filter = ['nickname']
    # 设置“动作”栏的位置
    actions_on_top = False
    actions_on_bottom = False
    list_display_links = ['nickname']
    # 可见不可修改
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['email']
        else:
            return []

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user_id', 'content', 'r_imagefield']
    # 在数据新增或修改的页面设置可看见的字段
    fields = ['title', 'user_id', 'content', 'r_imagefield']
    list_per_page = 100
    search_fields = ['title']
    list_filter = ['title']
    # 设置“动作”栏的位置
    actions_on_top = False
    actions_on_bottom = False
    list_display_links = ['title']
    # 可见不可修改
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['user_id']
        else:
            return []


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['recipe_id', 'user_id', 'comment', 'rating', 'create_data']
    # 在数据新增或修改的页面设置可看见的字段
    fields = ['recipe_id', 'user_id', 'comment', 'rating']
    list_per_page = 100
    search_fields = ['comment']
    list_filter = ['comment']
    # 设置“动作”栏的位置
    actions_on_top = False
    actions_on_bottom = False
    list_display_links = ['comment']
    # 可见不可修改
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['recipe_id', 'user_id', 'create_data']
        else:
            return []

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'recipe_id']
    # 在数据新增或修改的页面设置可看见的字段
    fields = ['user_id', 'recipe_id']
    list_per_page = 100
    search_fields = ['user_id']
    list_filter = ['user_id']
    # 设置“动作”栏的位置
    actions_on_top = False
    actions_on_bottom = False
    list_display_links = ['user_id']