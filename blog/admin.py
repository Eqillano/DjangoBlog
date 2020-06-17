from django.contrib import admin

# Register your models here.
from .models import *

#class PostAdmin(admin.ModelAdmin):
    #form = PostAdminForm()
    #save_as = True
    #prepoluated_fields = {"slug":{"title",}}
    #list_display = ('id,title,slug','category','created_at')
    #list_display_links = ('id','title')
    #list_filter = ('category')
#    readonly_fields = ('views','created_at')
#
#class CategoryAdmin(admin.ModelAdmin):
    #prepoluated_fields = {"slug":{"title",}}

#class TagAdmin(admin.ModelAdmin):
    #prepoluated_fields = {"slug":{"title",}}



admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
