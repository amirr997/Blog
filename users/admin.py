from django.contrib import admin
from .models import Profile, DirectMessages, ChatList

admin.site.register(Profile)
admin.site.register(ChatList)
admin.site.register(DirectMessages)
