from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Article


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'article_create.html')
    article_data = {
        'description': request.POST.get('description'),
        'details': request.POST.get('details'),
        'status': request.POST.get('status'),
        'done_date': request.POST.get('done_date')
    }
    article = Article.objects.create(**article_data)
    return redirect(reverse("detail_task", kwargs={'pk': article.pk}))


def detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'article_detail.html', context=context)


def delete_view(request):
    article_pk = request.GET.get('pk')
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/')


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
