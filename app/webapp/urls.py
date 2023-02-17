from django.urls import path

from webapp.views import base, articles

urlpatterns = [
    path("", base.index_view, name="index_page"),
    path('article/add/', articles.add_view, name="add_task"),
    path('article/<int:pk>', articles.detail_view, name='detail_task'),
    path('article/delete/', articles.delete_view, name='delete_task')
]
