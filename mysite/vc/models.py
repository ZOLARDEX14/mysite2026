from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Discounted Price")
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Original Price")
    image_url = models.CharField(max_length=500, blank=True, verbose_name="Image URL/Path")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.0, verbose_name="Rating")
    sales_count = models.IntegerField(default=0, verbose_name="Sales Count")
    stock = models.IntegerField(default=10, verbose_name="Stock")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Category")
    location = models.CharField(max_length=100, default='กรุงเทพมหานคร', verbose_name="Shipping Location")
    is_featured = models.BooleanField(default=False, verbose_name="Featured Product")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    @property
    def discount_percent(self):
        if self.original_price and self.original_price > self.price:
            discount = ((self.original_price - self.price) / self.original_price) * 100
            return int(round(discount))
        return 0

    def __str__(self):
        return self.name
