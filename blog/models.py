from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.category

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.CharField(max_length=2000)
    title = models.CharField(max_length=500)
    small_description = models.TextField()
    description = models.TextField()
    quote = models.CharField(max_length=2000)
    blog_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Comments(models.Model):
    blog_id = models.IntegerField()
    comment = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.CharField(max_length=255, null=True,blank=True)
    agree = models.BooleanField(default=False, null=True,blank=True)




