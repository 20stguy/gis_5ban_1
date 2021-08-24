from django.urls import path

from projectapp.views import SubscriptionListView
from subscribeapp.views import SubscriptionView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/<int:project_pk>', SubscriptionView.as_view(), name='subscirbe'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]