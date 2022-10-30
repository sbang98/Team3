from django.shortcuts import render
from progress.models import Post


def progress_list(request):
    post1 = Post.objects.get(pk=1)
    post2 = Post.objects.get(pk=2)
    post3 = Post.objects.get(pk=3)
    post4 = Post.objects.get(pk=4)
    post5 = Post.objects.get(pk=5)
    return render(request, 'progress_list.html', {'post1': post1, 'post2': post2, 'post3': post3, 'post4': post4, 'post5': post5})


def step_1(request):
    post = Post.objects.get(pk=1)
    return render(request, 'step_1.html', {'post': post})


def step_2(request):
    post = Post.objects.get(pk=2)
    return render(request, 'step_2.html', {'post': post})


def step_3(request):
    post = Post.objects.get(pk=3)
    return render(request, 'step_3.html', {'post': post})


def step_4(request):
    post = Post.objects.get(pk=4)
    return render(request, 'step_4.html', {'post': post})


def step_5(request):
    post = Post.objects.get(pk=5)
    return render(request, 'step_5.html', {'post': post})
