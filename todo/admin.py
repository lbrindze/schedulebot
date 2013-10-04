from django.contrib import admin
from todo.models import Item, ItemAdmin, DateTime, DateAdmin

admin.site.register(Item, ItemAdmin)
admin.site.register(DateTime, DateAdmin)