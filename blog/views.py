from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post , Category
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def blog(req):
    posts = Post.objects.order_by('-date')

    paginator = Paginator(posts, 6)
    
    page = req.GET.get('page')

    posts = paginator.get_page(page)

    categories = Category.objects.all()

    return render(req, 'blog/blog.html' , {'posts': posts, 'categories' : categories})


def blog_en(req):
    posts = Post.objects.order_by('-date')

    paginator = Paginator(posts, 6)
    
    page = req.GET.get('page')

    posts = paginator.get_page(page)

    categories = Category.objects.all()

    return render(req, 'blog/blog-en.html' , {'posts': posts, 'categories' : categories}
)

def category(req, cat):
    posts = Post.objects.filter(categories__icontains=cat).order_by('-date')

    paginator = Paginator(posts, 6)
    
    page = req.GET.get('page')

    posts = paginator.get_page(page)

    categories = Category.objects.all()

    return render(req, 'blog/category.html' , {'posts': posts, 'categories' : categories})


def category_en(req, cat):
    posts = Post.objects.filter(categories__icontains=cat).order_by('-date')

    paginator = Paginator(posts, 6)
    
    page = req.GET.get('page')

    posts = paginator.get_page(page)

    categories = Category.objects.all()

    return render(req, 'blog/category-en.html' , {'posts': posts, 'categories' : categories})

    

def blog_search(req):

    search = req.GET.get('search')

    posts = Post.objects.filter(Q(description__icontains=search) | Q(title__icontains=search)).order_by('-date')

    paginator = Paginator(posts, 6)
    
    page = req.GET.get('page')

    posts = paginator.get_page(page)

    categories = Category.objects.all()

    return render(req, 'blog/blog-search.html' , {'posts': posts, 'categories' : categories})


def blog_search_en(req):
    search = req.GET.get('search')

    posts = Post.objects.filter(Q(description__icontains=search) | Q(title__icontains=search)).order_by('-date')

    paginator = Paginator(posts, 6)
    
    page = req.GET.get('page')

    posts = paginator.get_page(page)

    categories = Category.objects.all()

    return render(req, 'blog/blog-search-en.html' , {'posts': posts, 'categories' : categories}
)



def post(req, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(req, 'blog/post.html' , {'post': post}
)
def post_en(req, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(req, 'blog/post-en.html' , {'post': post}
)
