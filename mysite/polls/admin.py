from django.contrib import admin
from .models import TasksList, VariantsList, EventTpl, Policy, Object, Tag

admin.site.register(TasksList)
admin.site.register(VariantsList)
admin.site.register(EventTpl)
admin.site.register(Policy)
admin.site.register(Object)
admin.site.register(Tag)
