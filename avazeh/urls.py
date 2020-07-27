"""avazeh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views as portfolio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_views.home, name='home'),
    path('en/', portfolio_views.home_en, name='home-en'),
    path('about/', portfolio_views.about, name='about'),
    path('about/en/', portfolio_views.about_en, name='about-en'),
    path('products/', portfolio_views.products, name='products'),
    path('products/en/', portfolio_views.products_en, name='products-en'),
    path('products/<int:product_id>/', portfolio_views.product , name='product'),
    path('products/en/<int:product_id>/', portfolio_views.product_en , name='product-en'),

    path('contact/', portfolio_views.contact, name='contact'),
    path('contact/msg-sent', portfolio_views.msg_sent, name='msg-sent'),
    path('contact/en/', portfolio_views.contact_en, name='contact-en'),
    path('blog/', include('blog.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)