from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post


def home(request):
    return render(request, 'home.html')

@login_required
def form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)  # Formani POST ichida yaratish yaxshiroq
        if form.is_valid():
            # 1. Formadan model obyektini olamiz, lekin bazaga hali saqlamaymiz
            post = form.save(commit=False)

            # 2. Model maydoniga foydalanuvchini biriktiramiz
            post.created_by = request.user

            # 3. Endi bazaga saqlaymiz
            post.save()

            return redirect('home')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'form.html', context)

@login_required
def post_list_id(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'post_list_id.html', context=context)

@login_required
def post_list_slug(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post_list_slug.html', context=context)

@login_required
def post_detail_with_id(request,id):
    post = get_object_or_404(Post, id=id)
    context = {'post': post}
    return render(request, 'post_detail_id.html', context=context)

@login_required
def post_detail_with_slug(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post':post}
    return render(request, 'post_detail_slug.html', context=context)


def post_delete_id(request,id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.is_active = False
        post.save()
        return redirect('post_list_id')
    context = {
        'post':post
    }
    return render(request,'post_delete.html',context)


def update_post_id(request,id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list_id')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request,'post_update_id.html',context)

