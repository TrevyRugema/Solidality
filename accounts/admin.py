from django.contrib import admin
from accounts.auth.models import User
from django.contrib.auth import get_user_model

@admin.register(User)
class MemberAdmin(admin.ModelAdmin):
    list_display=['id','username','email']
    list_filter=['username','email']
    search_fields=['id','firs_name']
    list_display_links=['id','email']
    list_per_page=10

