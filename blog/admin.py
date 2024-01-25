from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    '''
    Fileds will show up in Admin panel. This code has been copied
    from Code Institutes walktrough project:
    https://github.com/Code-Institute-Solutions/Django3blog/tree/master/11_messages/blog
    '''
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on',)
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
