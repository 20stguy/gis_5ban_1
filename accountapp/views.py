from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.models import HelloWorld
from accountapp.forms import AccountCreationForm
from articleapp.models import Article


# hello_world 삭제
# @login_required
# def hello_world(request):
#     if request.method == "POST":
#         temp = request.POST.get('hello_world_input')
#         # temp에서 받은걸 new_hello_world에 넣어준다
#         new_hello_world = HelloWorld()
#         # model에 넣어준다
#         new_hello_world.text = temp
#         new_hello_world.save()
#         return HttpResponseRedirect(reverse('accountapp:hello_world'))
#     else:
#         hello_world_list = HelloWorld.objects.all()
#         return render(request, 'accountapp/hello_world.html',
#                       context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list') #로그인시 연결되는 프로그램은 accountapp:hello_world)
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user' # 타겟 유저를 통해 html 볼 수 있다
    template_name = 'accountapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=object)
        return super().get_context_data(object_list=article_list, **kwargs)

has_ownership = [login_required, account_ownership_required]


# has_ownership으로 대체한다
# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# # 계정관련 decorators.py에 decorator 만들고 불러오기.
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk}) # self.object = target_user를 받는다.


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})



    # decorator로 대체(장고에서 기본적으로 제공하는 decorator 있다)
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated and self.get_object() == request.user:
#             return super().get(request, *args, **kwargs)
# #     def와 return 두줄은 부모 calss와 같은것으로 지우나 쓰나 구동에 바뀌는게 없다
#         else:
#             return HttpResponseForbidden()
#
#     def post(self, request, *args, **kwargs):
#             if request.user.is_authenticated and self.get_object() == request.user:
#                 return super().get(request, *args, **kwargs)
#                 #     def와 return 두줄은 부모 calss와 같은것으로 지우나 쓰나 구동에 바뀌는게 없다
#             else:
#                 return HttpResponseForbidden()


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
# has_ownership으로 대체한다
# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy = ('articleapp:list')
    template_name = 'accountapp/delete.html'
    # decorator로 대체(장고에서 기본적으로 제공하는 decorator 있다)
    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().get(request, *args, **kwargs)
    #         #     def와 return 두줄은 부모 calss와 같은것으로 지우나 쓰나 구동에 바뀌는게 없다
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.get_object() == request.user:
    #         return super().get(request, *args, **kwargs)
    #         #     def와 return 두줄은 부모 calss와 같은것으로 지우나 쓰나 구동에 바뀌는게 없다
    #     else:
    #         return HttpResponseForbidden()



