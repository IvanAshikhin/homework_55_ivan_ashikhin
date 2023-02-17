from django.urls import path

from webapp.views import base, articles

urlpatterns = [
    path("", base.index_view),
    path('article/add/', articles.add_view),
    path('article/<int:pk>', articles.detail_view),
    path('article/delete/', articles.delete_view)
]
