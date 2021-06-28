from snippets.models import Snippet
from django.contrib import admin
from .models import Snippet,User

# Register your models here.

admin.site.register(Snippet)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass