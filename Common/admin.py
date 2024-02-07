from django.contrib import admin
from .models import  Post , Profile , Skill , About , Service , Category , Portfolio

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'description' , 'author' , 'image' , 'view_counts' , 'id' , ) 
    list_display_links = ('title' , 'image')
    search_fields = ('title',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name' , 'image' , 'bio')
    list_display_links = ('full_name' , 'image')
    search_fields = ('full_name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title','percentage','order')
    list_display_links = ('title',)
    search_fields = ('title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('experience' , 'total_project' , 'total_users' , 'salary')
    list_display_links = ('total_project','total_users','salary')
    search_fields = ('total_project','total_users','salary')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','icon','description')
    list_display_links = ('title',)
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','description','image','link','category','completed_at')
    list_display_links = ('title','image','link','category')
    search_fields = ('title','link','used_tools','category')