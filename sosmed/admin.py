# sosmed/admin.py
from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Instagram

class CustomAdminSite(AdminSite):
    site_header = 'ELECTRIC XTRA - Admin Panel'
    site_title = 'Social Media Manager'
    index_title = 'Dashboard'

# Register model
@admin.register(Instagram)
class InstagramAdmin(admin.ModelAdmin):
    list_display = ['nama_depan', 'nama_belakang', 'username']
    search_fields = ['nama_depan', 'nama_belakang', 'username']
    list_per_page = 20