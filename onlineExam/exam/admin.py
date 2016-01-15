from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *;

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	search_fields=['news']
	ordering=('-publishDate',)

class UserProfileInline(admin.StackedInline):
    # list_display = ('user' 'website')
    # search_fields = ['user']
    # form = MyUserChangeForm
    # add_form = MyUserCreationForm
    model=UserProfile
    list_display=['college','faculty','phone','joined_date']
    can_delete = False
    verbose_name_plural = 'UserProfile'
class UserAdmin(BaseUserAdmin):
	BaseUserAdmin.list_display += ('get_college','get_faculty','get_date')
	inlines = (UserProfileInline,)
	list_filter = ('username',)
	search_fields = ('username',)
	ordering = ('-is_superuser','-is_active','username')

	def  get_college(self, obj):
		return UserProfile.objects.get(user=obj).college
	def get_faculty(self, obj):
		return UserProfile.objects.get(user=obj).faculty
	def get_phone(self, obj):
		return UserProfile.objects.get(user=obj).phone
	def get_date(self,obj):
		return UserProfile.objects.get(user=obj).joined_date

class KeyAdmin(admin.ModelAdmin):
	search_fields=['key']
	list_display=['key','status']
	ordering=('-status',)

admin.site.register(News,NewsAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Key, KeyAdmin)
