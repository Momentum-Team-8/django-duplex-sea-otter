from snippets.models import Snippet
from django.contrib import admin
from .models import Snippet,User,Category

# Register your models here.

admin.site.register(Snippet)
admin.site.register(Category)



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass