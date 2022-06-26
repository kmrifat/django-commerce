from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class Brand(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "brands"


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    sort_order = models.IntegerField(default=0)
    image = models.ImageField(help_text='Category Image', null=True, blank=True)

    class Meta:
        db_table = "categories"


class Product(models.Model):
    PRODUCT_TYPE = (
        ('physical', 'Physical'),
        ('digital', 'Digital'),
    )

    name = models.CharField(max_length=255, help_text='Product Name')
    product_type = models.CharField(max_length=255, choices=PRODUCT_TYPE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category, db_table='product_categories')
    visible = models.BooleanField(default=True, help_text='Visible on Storefront')
    description = HTMLField()

    class Meta:
        db_table = 'products'


class ProductImage(models.Model):
    image = models.ImageField()
    description = models.CharField(max_length=255)
    thumbnail = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'


class ProductIdentifier(models.Model):
    sku = models.SlugField()
    mpn = models.CharField(max_length=255, help_text='Manufacturer Part Number (MPN)', blank=True, null=True)
    upc = models.CharField(max_length=255, help_text='Product UPC/EAN', null=True, blank=True)
    gtin = models.CharField(max_length=255, help_text='Global Trade Item Number', null=True, blank=True)
    bpn = models.CharField(max_length=255, help_text='Bin Picking Number (BPN)', null=True, blank=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_identifier'


class ProductPrice(models.Model):
    default_price = models.FloatField()
    cost = models.FloatField(default=0)
    msrp = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_price'


class ProductDiscount(models.Model):
    DISCOUNT_TYPE_CHOICE = (
        ('% Discount', 'percentage'),
        ('Fixed Amount', 'fixed'),
    )
    discount_type = models.CharField(max_length=255, choices=DISCOUNT_TYPE_CHOICE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_discount'


class ProductDiscountPrice(models.Model):
    discount = models.ForeignKey(ProductDiscount, on_delete=models.CASCADE)
    min_quantity = models.IntegerField(default=2, help_text='Min Quantity')
    discount_unit = models.FloatField(default=0, help_text='Discount Unit By Discount Type Choice')
    discount_price = models.FloatField(default=0, help_text='Discount Price')

    class Meta:
        db_table = 'product_discount_prices'


class ProductShipping(models.Model):
    shipping_price = models.FloatField()
    free_shipping = models.BooleanField(default=False)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_shipping'


class ProductPurchasable(models.Model):
    min_qt = models.FloatField(help_text='Minimum Purchase Quantity', blank=True, null=True)
    max_qt = models.FloatField(help_text='Maximum Purchase Quantity', blank=True, null=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_purchasable'


class ProductSeo(models.Model):
    page_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.CharField(max_length=255, null=True, blank=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_seo'


class ProductReview(models.Model):
    ratting = models.IntegerField()
    review = models.TextField()
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_reviews'
