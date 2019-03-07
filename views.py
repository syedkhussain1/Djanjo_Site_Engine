import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    index_html = open("content/index.html").read()
    context = {
        "content": index_html
    }
    return render(request, "base.html", context)

def my_projects(request):
    project_html = open("content/project.html").read()
    context = {
        "content": project_html
    }
    return render(request, "base.html", context)

def my_blog(request):
    blog_html = open("content/blog.html").read()
    context = {
        "content": blog_html
    }
    return render(request, "base.html", context)


# def github_api_example(request):
#     # We can also combine Django with APIs
#     response = requests.get('https://api.github.com/users/michaelpb/repos')
#     repos = response.json()
#     context = {
#         'github_repos': repos,
#     }
#     return render(request, 'github.html', context)

