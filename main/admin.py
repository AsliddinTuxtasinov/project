from django.contrib import admin
from main.models import Catagory, Post


class Admin_catagory(admin.ModelAdmin):
    prepopulated_fields = {"slug_catagory":("catagory",)}

class Admin_Post(admin.ModelAdmin):
    prepopulated_fields = {"slug_post":("title",)}


admin.site.register(Catagory, Admin_catagory)
admin.site.register(Post, Admin_Post)