from django.contrib import admin
from .models import Member
from django.contrib.auth import get_user_model
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display=['id','username','email','role']
    list_filter=['username','role']
    search_fields=['id','firs_name']
    list_display_links=['id','email','role']
    list_per_page=10

