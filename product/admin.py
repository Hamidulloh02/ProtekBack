from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Product, Description,Brand, Productclass, Category, Topproduct, OnlyOneProduct
from django.utils.html import mark_safe


# Register your models here.
class DescriptionInline(admin.TabularInline):
    model = Description
    extra = 1

class TechnicalSpecifications(admin.ModelAdmin):
    inlines = [DescriptionInline]
    readonly_fields = ('updated_at', 'created_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):  # `TechnicalSpecifications, TranslationAdmin` kerak bo‘lsa, qo‘shing
    list_display = ('image_tag', 'title')  # ✅ Rasmni chiqarish uchun `image_tag` qo‘shildi
    languages = ('uz', 'ru')

    def image_tag(self, obj):  # ✅ `Product` emas, `obj` bo‘lishi kerak
        if obj.img:  # Rasm borligini tekshiramiz
            return mark_safe(f'<img src="{obj.img.url}" width="80" height="80" style="object-fit:cover; border-radius:5px;" />')
        return "No Image"

    image_tag.short_description = "Image"  # Admin panelda ustun nomi
    search_fields = ('title', 'description')
    list_filter = ('brand', 'category', 'productclass')
    list_display_links = ('title', 'image_tag')
    list_per_page = 10



admin.site.register(Brand)
admin.site.register(Productclass)
admin.site.register(Category)
admin.site.register(Topproduct)
admin.site.register(OnlyOneProduct)


