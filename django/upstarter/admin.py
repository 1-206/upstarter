from django.contrib import admin

from .models import *


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Investment)
admin.site.register(Chat)
admin.site.register(Message)
