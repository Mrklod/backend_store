from django.contrib import admin

from users.models import User
from products.admin import BasketInline
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketInline,)