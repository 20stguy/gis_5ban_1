from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

# app 이름 accountapp -> name = router이름
app_name = 'accountapp'


urlpatterns = [
    # 주소창에 heello_world로 들가면, hello_worl의 충
    # name = router 이름
    # 삭제 path('hello_world/', hello_world, name='hello_world'), #name == router이름
    #
        path('login/', LoginView.as_view(template_name='accountapp/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    # detail view는 어느 정보를 보는지 특정해야 하므로<int:pk>라고 특정하였다
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),

    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),


]
