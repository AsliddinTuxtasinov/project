from django.shortcuts import render, get_object_or_404
from main.models import Catagory, Post
from django.db.models import Q


def index(request):
    posts = Post.objects.all()
    catagory = Catagory.objects.all()

    template_name = "index.html"
    return render(request, template_name, {
        "posts":posts,
        "catagory":catagory
    })


def catagorySlug(request, id):

    catagorya = get_object_or_404(Catagory, pk=id)
    posts = Post.objects.filter( catagory=catagorya )
    categoryalar = Catagory.objects.all()

    template_name = "index.html"
    return render(request,template_name, {
        "posts":posts,
        "catagory":categoryalar
    })

def postSlug(request, slug):
    post = Post.objects.get(slug_post=slug)
    catagory = Catagory.objects.all()

    template_name = "post-detal.html"
    return render(request,template_name, {
        "post":post,
        "catagory":catagory
    })


def search(request):
    category = Catagory.objects.all().order_by('catagory')
    search_post = request.GET.get('search')

    if search_post:
        posts = Post.objects.filter( Q(title__icontains=search_post) | Q(describetion__icontains=search_post) )
    else:
        posts = Post.objects.all()
    
    return render(request, "index.html", {
        "posts":posts,
        "catagory":category
    })