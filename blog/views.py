from django.shortcuts import render

posts = [
    {
        'author': 'AlfonsoB',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 25, 2022'
    },
    {
        'author': 'alfsbalao',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 26, 2022'
    }
]

def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})