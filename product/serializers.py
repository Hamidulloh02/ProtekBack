from rest_framework import serializers

from product.models import Product,Description,Category,Productclass,Brand,Topproduct,OnlyOneProduct

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')
class ClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productclass
        fields = ('id','name')
class BrandSerializers(serializers.ModelSerializer):
    class Meta :
        model = Brand
        fields = ('id','name')

class descriptionSerializers(serializers.ModelSerializer):
    class Meta :
        model = Description
        fields = ('id','post','dec_title','dec_info')
class TopproductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Topproduct
        fields = ('id','img','created_at','updated_at')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    productclass = ClassSerializers()
    description = descriptionSerializers(many=True)
    brand = BrandSerializers()
    
    title = serializers.SerializerMethodField()
    info = serializers.SerializerMethodField()
    descript_text = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'img', 'info', 'category', 'productclass', 'descript_text', 'description', 'brand')

    def get_title(self, obj):
        request = self.context.get('request', None)
        lang = request.GET.get('lang', 'en') if request else 'en'
        return getattr(obj, f'title_{lang}', obj.title)

    def get_info(self, obj):
        request = self.context.get('request', None)
        lang = request.GET.get('lang', 'en') if request else 'en'
        return getattr(obj, f'info_{lang}', obj.info)

    def get_descript_text(self, obj):
        request = self.context.get('request', None)
        lang = request.GET.get('lang', 'en') if request else 'en'
        return getattr(obj, f'descript_text_{lang}', obj.descript_text)


    
class OnlyOneProSerializers(serializers.ModelSerializer):
    productclass = ClassSerializers()
    class Meta:
        model = OnlyOneProduct
        fields = ('img','productclass')