from django.contrib import admin

# Register your models here.
from product.models import Product, Category, Brand, ProductImage, ProductIdentifier, ProductPrice, ProductPurchasable, \
    ProductSeo, ProductDiscount, ProductDiscountPrice


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductIdentifierInline(admin.TabularInline):
    model = ProductIdentifier


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice


class ProductPurchasableInline(admin.TabularInline):
    model = ProductPurchasable


class ProductSeoInline(admin.TabularInline):
    model = ProductSeo


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductPriceInline, ProductImageInline,
               ProductPurchasableInline, ProductIdentifierInline, ProductSeoInline)


class ProductDiscountPriceInline(admin.TabularInline):
    model = ProductDiscountPrice


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    inlines = (ProductDiscountPriceInline,)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
