from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
	articles = models.Article.objects.all()
	return render(request, 'blog/index.html', {'articles':articles})

def article_page(request, article_id):
	article = models.Article.objects.get(pk=article_id)
	return render(request, 'blog/article_page.html', {'article':article})


def edit_page(request, article_id):
	if str(article_id) == '0':#0表示新建 其他表示修改先有文章
		return render(request, 'blog/edit_page.html')
	else:
		article = models.Article.objects.get(pk=article_id)
		return render(request, 'blog/edit_page.html', {'article':article})


def edit_action(request):
	title = request.POST.get('title', 'TITLE')
	content = request.POST.get('content', 'CONTENT')
	article_id = request.POST.get('article_id', '0')

	if str(article_id) == '0':
		models.Article.objects.create(title=title, content=content)
		articles = models.Article.objects.all()
		return render(request, 'blog/index.html', {'articles': articles})
	else:
		article = models.Article.objects.get(pk=article_id)
		article.title = title
		article.content = content
		article.save()
		return render(request, 'blog/article_page.html', {'article':article})
