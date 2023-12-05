from django.contrib import admin
from .models import Event, Membership
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    prepopulated_fields={'slug': ('title',)}
    list_filter=('status', 'created_on',)
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'body', 'post', 'created_on', 'approved')
#     list_filter = ('approved', 'created_on')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']


#     def approve_comments(self, request, queryset):
#         queryset.update(approved=True)

# This is for admin to see members and administrate members
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
   list_display = ('name', 'last_name', 'memberlevel', 'created_on')
   search_fields = ('name', 'email', 'memberlevel')
