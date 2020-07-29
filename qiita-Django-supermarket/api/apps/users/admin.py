from django.contrib import admin

from .models import VerifyCode, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthday', 'mobile', 'gender', 'email']


class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'mobile', 'add_time']


admin.site.register(VerifyCode, VerifyCodeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
