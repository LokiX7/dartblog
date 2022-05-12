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
        'category',
        'is_published',
    )
    
    fields = (
        'title',
        'slug',
        'category',
        'content',
        'tags',
        'get_image',
        'photo',
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
    actions = ['make_selected_published', 'make_selected_unpublished']

    def get_image(self, obj):
        """Get image for post create form"""
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='250' height=250>")
        
        else:
            return '-'

    def get_preview(self, obj):
        """Get image for admin display"""
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50' height=50>")
        
        else:
            return '-'

    get_preview.short_description = 'image'

    def make_selected_published(self, request, queryset):
        """Make post published"""
        queryset.update(is_published=True)

    def make_selected_unpublished(self, request, queryset):
        """Make post unpublished"""
        queryset.update(is_published=False)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
