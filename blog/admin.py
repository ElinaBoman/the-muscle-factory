from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    prepopulated_fields={'slug': ('title',)}
    list_filter=('status', 'created_on',)
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']


# This is for admin to see members and administrate members


