from django.db import models

# Create your models here.
class Product(models.Model):
    catogries = [
        ("الهواتف","الهواتف"),
        ("الإكسسوارات","الإكسسوارات"),
        ("الحواسيب","الحواسيب"),

    ]
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=9)
    img = models.ImageField(upload_to='photos/%y/%m/%d')
    catogry = models.CharField(null=True,blank=True,choices=catogries)
    count = models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    userName = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    email = models.EmailField()
    prodects = models.ManyToManyField(Product,null=True)
    

    def __str__(self):
        return self.userName






# models.py
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='categories/')
    is_featured = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    main_image = models.ImageField(upload_to='products/')
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_count = models.PositiveIntegerField(default=0)
    
    @property
    def discount_percentage(self):
        if self.discount_price:
            return int(((self.price - self.discount_price) / self.price) * 100)
        return None
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='blog/')
    content = models.TextField()
    excerpt = models.TextField(max_length=300)
    is_published = models.BooleanField(default=True)
    publish_date = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

