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
        'status',
        'get_preview',
    )

    list_display_links = (
        'title',
    )

    list_filter = (
        'category',
        'status',
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
        'status',
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
        'make_selected_published', 
        'make_selected_pinned',
        'make_selected_unpublished',
    ]

    def make_selected_published(self, request, queryset):
        """Make post published"""
        queryset.update(status=Post.PUBLISHED)

    def make_selected_pinned(self, request, queryset):
        """Make post published and pinned"""
        queryset.update(status=Post.PINNED)

    def make_selected_unpublished(self, request, queryset):
        """Make post unpublished"""
        queryset.update(status=Post.UNPUBLISHED)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
