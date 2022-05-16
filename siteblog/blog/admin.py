from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Tag, Post


class PostAdminForm(forms.ModelForm):
    """Add CKEditor to post create form"""
    content = forms.CharField(widget=CKEditorUploadingWidget)
    
    class Meta:
        model = Post
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    
    list_display = (
        'id',
        'title',
        'category',
        'author',
        'created_at',
        'views',
        'rating',
        'is_published',
        'get_preview',
    )

    list_display_links = (
        'title',
    )

    list_filter = (
        'is_published',
        'category',
        'tags',
    )
    
    fields = (
        'title',
        'slug',
        'category',
        'content',
        'tags',
        'get_image',
        'image',
        'author',
        'is_published',
        'views',
        'rating',
        'created_at',
    )
    
    readonly_fields = [
        'views', 
        'rating', 
        'get_image', 
        'get_preview',
        'created_at',
    ]

    def get_image(self, obj):
        """Get image for post create form"""
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='250' height=250>")
        
        else:
            return '-'

    def get_preview(self, obj):
        """Get image for admin display"""
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='25' height=25>")
        
        else:
            return '-'

    get_preview.short_description = 'image'
    
    actions = [
        'make_published',
        'make_unpublished',
    ]
    
    @admin.action(description='Mark selected stories as published')
    def make_published(self, request, queryset):
        queryset.update(is_published=True)

    @admin.action(description='Mark selected stories as unpublished')
    def make_unpublished(self, request, queryset):
        queryset.update(is_published=False)
        

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
