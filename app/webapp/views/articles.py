from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Article

from webapp.forms import ArticleForm


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, 'article_create.html', context={'form': form})
    form = ArticleForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'article_create.html', context={'form': form})
    else:
        article = Article.objects.create(**form.cleaned_data)
        return redirect(reverse("detail_task", kwargs={'pk': article.pk}))


def detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'article_detail.html', context=context)


def update_view(requset, pk):
    article = get_object_or_404(Article, pk=pk)
    if requset.method == "POST":
        article.description = requset.POST.get('description')
        article.details = requset.POST.get('details')
        article.status = requset.POST.get('status')
        article.done_date = requset.POST.get('done_date')
        article.save()
        return redirect('detail_task', pk=article.pk)
    return render(requset, 'task_update.html', context={'article': article})


def delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_confitm_delete.html', context={"article": article})


def confirm_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('index_page')
