from django.shortcuts import render
from django.views.generic import (ListView)
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'homepage/article.html'     #Open View visiting domain showing recent articles
    context_object_name = 'articles'            #Use this name in your html templates for showing one set of data
    ordering = ['-date_posted']
    # paginated_by = 10
