from django.shortcuts import render
from .models import Product
from django.db.models import Q
from .models import Products, Category
from .models import BlogPost
from django.core.paginator import Paginator
# Create your views here.

def login(request):
    return render(request,'product/login.html')

def signin(request):
    return render(request,'product/signin.html')

def home(request):
    # Featured categories (you can modify this query as needed)
    featured_categories = Category.objects.filter(is_featured=True)[:4]
    
    # Featured products
    featured_products = Products.objects.filter(is_featured=True, is_active=True)[:8]
    
    # New products
    new_products = Products.objects.filter(is_active=True).order_by('-created_at')[:8]
    
    # Latest blog posts
    latest_posts = BlogPost.objects.filter(is_published=True).order_by('-publish_date')[:3]
    
    context = {
        'featured_categories': featured_categories,
        'featured_products': featured_products,
        'new_products': new_products,
        'latest_posts': latest_posts,
    }
    return render(request, 'product/home.html', context)

def products(request):
    return render(request,'product/products.html',{'product':Product.objects.all()})


def product_search(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', None)
    
    products = Products.objects.filter(is_active=True)
    
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )
    
    if category:
        products = products.filter(category__slug=category)
    
    context = {
        'products': products,
        'query': query,
        'category': category
    }
    return render(request, 'product/search.html', context)


def about(request):
    context = {
        'team_members': [
            {
                'name': 'أحمد محمد',
                'position': 'المدير التنفيذي',
                'bio': 'خبير في التجارة الإلكترونية مع أكثر من 10 سنوات خبرة',
                'image': 'team/ahmed.jpg'
            },
            {
                'name': 'امين الصلاحي',
                'position': 'رئيس قسم التكنولوجيا',
                'bio': 'متخصص في تطوير حلول التجارة الإلكترونية',
                'image': 'team/sara.jpg'
            }
        ],
        'stats': {
            'customers': 10000,
            'products': 500,
            'years': 5,
            'awards': 3
        }
    }
    return render(request, 'product/about.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug, is_active=True)
    return render(request, 'product/detail.html', {'product': product})


def category_products(request, slug):
    """
    عرض المنتجات حسب الفئة
    """
    category = get_object_or_404(Category, slug=slug)
    products = Products.objects.filter(category=category, is_active=True)
    
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'product/category_products.html', context)