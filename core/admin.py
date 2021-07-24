from django.contrib import admin
from .models import Client
from .models import images
from .models import user

class ClientAdmin(admin.ModelAdmin):
	fields = ['name','age','salary','anand']
	list_display = ['name','age','salary','anand']
	list_display = ['name','age','salary','anand']
	search = ['name','age','salary','anand']



# class ClientAdmin(admin.ModelAdmin):
# 	fields = ['name','age','salary','anand']

admin.site.register(Client,ClientAdmin)

admin.site.register(images)
admin.site.register(user)
