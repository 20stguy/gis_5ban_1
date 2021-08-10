from django.contrib.auth.forms import UserCreationForm

# views.py에 있는 class UpdateView안에있는(ctrl + b)
class AccountCreationForm(UserCreationForm):
    # 덮어씌우기
    # 초기화함수
    def __init__(self, *args, **kwargs):
        # 부모클래스의 메서드 접근하기 super
        super().__init__(*args, **kwargs)

        # 본인 객체내에서 fields를 찾아 username을 보이지 않게 함
        self.fields['username'].disabled = True