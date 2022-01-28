import admin_thumbnails
from django.contrib import admin
from .models import *
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
@admin_thumbnails.thumbnail('image')
class PostImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 3


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','image_thumbnail']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','category', 'author']
    list_filter = ['category']
    inlines = [PostImageInline]

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)


admin.site.register(Post, PostAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Like)