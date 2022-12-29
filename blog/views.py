from django.shortcuts import render, redirect
from .models import Blog,Category, Comments
import math

# Create your views here.


def Blogs(request):
    side_data = Blog.objects.all()
    category  = Category.objects.all()
    tags = Category.objects.all()
    no_of_posts = 3
    # if request.GET[']:
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    print(page)
    print(request.GET)
    blogs = Blog.objects.all()
    length = len(blogs)
    print(length)
    blogs = blogs[(page-1)*no_of_posts: page*no_of_posts]
    if page > 1:
        prev = page -1
    else:
        prev = None
    if page < math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    context = {'blog':blogs, 'side_data':side_data, 'category':category , 'tags':tags, 'prev':prev, 'nxt':nxt}

    return render(request, 'blogs/blogs.html', context)







def BlogDetail(request, id):
    blogs_detail = Blog.objects.filter(id=id)
    length = len(blogs_detail)
    blog_data = Blog.objects.get(id=id)
    blogs = Blog.objects.all()
    category = Category.objects.all()
    tags = Category.objects.all()
    comments = Comments.objects.filter(id=id)
    comments2 = Comments.objects.filter(id=id)

    if request.method == "POST":
        blog_id = request.POST.get('blog_id')
        comment = request.POST.get('comment')
        name = request.POST.get('author')
        email = request.POST.get('email')
        website = request.POST.get('url')
        agree = request.POST.get('wp-comment-cookies-consent')
        data = Comments(comment=comment, name=name,email=email, website=website,agree=agree, blog_id=blog_id)
        data.save()
        return redirect('blogs/blog')
        print(data)



    context = {'blog_detail':blogs_detail, 'blog_data':blog_data, 'blogs':blogs, 'category':category, 'tags':tags, 'comments':comments, 'comments2':comments2, 'length':length}
    return render(request, 'blogs/blog_detail.html', context)



def search(request):
    search = request.GET['search']
    side_data = Blog.objects.filter(title__icontains=search)
    print(side_data, '=================>')
    no_of_posts = 3
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    print(page)
    print(request.GET)
    blogs = Blog.objects.all()
    length = len(blogs)
    print(length)
    blogs = blogs[(page - 1) * no_of_posts: page * no_of_posts]
    if page > 1:
        prev = page - 1
    else:
        prev = None
    if page < math.ceil(length / no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    return render(request, 'blogs/search.html', context={'side_data':side_data, 'prev':prev, 'nxt':nxt})