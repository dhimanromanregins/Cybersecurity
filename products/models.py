from django.db import models
# Create your models here.
class ProductCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

class ProductTags(models.Model):
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.tags

class Products(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    tags = models.ForeignKey(ProductTags, on_delete=models.CASCADE)
    image = models.CharField(max_length=10000)
    product_name = models.CharField(max_length=500)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    small_description = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.product_name


class ProductReview(models.Model):
    product_id = models.IntegerField()
    review = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    agree = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name





