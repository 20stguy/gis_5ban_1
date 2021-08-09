from django.urls import path

from commentapp.views import CommentCreateView

app_name = 'commentapp'

urlpatterns = [
  path('creat', CommentCreateView.as_view, name='create'),

]