from django.contrib import admin

# Register your models here.
from messagesuser.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'sent_date')
    list_filter = ('name', 'sent_date', 'email')
    search_fields = ('email', 'name')


admin.site.register(Message, MessageAdmin)
