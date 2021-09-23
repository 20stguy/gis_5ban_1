from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


class SubscriptionView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        project = Project.objects.get(pk=kwargs['project_pk'])

        # 구독정보를 먼저 찾는다.
        subscription = Subscription.objects.filter(user=user,
                                                       project=project)

        # 구독정보는 회원만 할 수 있어야 하므로 user가 로그인 되어있느지 부터 확인
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super().get(request, *args, **kwargs)

        def get_redirect_url(self, *args, **kwargs):
            return reverse('projectapp:detail', kwargs={kwargs['pk: kwargs']})


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'articel_list'
    template_name = 'subscribeapp/list.html'

    paginate_by = 20

    def get_queryset(self):
        project_list = Subscription.objects.filter(user=self.request.user).values_list('project')
        # Field Lookup기능 project__in => SQL에서 SELECT ... WHERE Project, ... 과 같다.
        article_list = Article.objects.filter(project__in=project_list)
        return article_list

