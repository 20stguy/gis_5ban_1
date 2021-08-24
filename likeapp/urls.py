from django.urls import path

urlpatterns = [
    path('article/<int:article_pk>', LikeArticleView.as_view(), name='article_like'),

]