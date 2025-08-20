from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('/create_Acount/',views.signin,name='signin'),
    # path('/home/',views.home,name='home'),
    path('/products/',views.products,name='products'),
    path('/login/',views.login,name='login'),
    path('/search/', views.product_search, name='product_search'),
    path('/about/', views.about, name='about'),
    path('/products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),


]