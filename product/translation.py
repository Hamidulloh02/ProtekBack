from modeltranslation.translator import register, TranslationOptions
from .models import Product, Productclass

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'info', 'descript_text')

@register(Productclass)
class ProductclassTranslationOptions(TranslationOptions):  # Nomi o‘zgartirildi
    fields = ('name',)
