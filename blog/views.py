from django.shortcuts import render

posts = [
    {
        'author': 'Hemank',
        'title': 'Blog Post1',
        'content': 'First post content',
        'date_posted': 'January 1, 2025',
    },
    {
        'author': 'Jam',
        'title': 'Blog Post',
        'content': 'Second post content',
        'date_posted': 'January 10, 2025',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})