from django.contrib import admin
from .models import Membership

# Register your models here.

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
   list_display = ('name', 'last_name', 'memberlevel', 'created_on')
   search_fields = ('name', 'email', 'memberlevel')