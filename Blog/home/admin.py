from django.contrib import admin

# Register your models here.
from .models import BlogModel

@admin.register(BlogModel)
    
class BlogAdmin(admin.ModelAdmin):
    list_display=['uuid','user','title','blog_text','main_image']
