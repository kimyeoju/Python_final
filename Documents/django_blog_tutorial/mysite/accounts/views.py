from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.conf import settings

# urlpatter을 깔끔하게 하기 위해서 클래스뷰로 할당
signup = CreateView.as_view(
    form_class = UserCreationForm,
    #기본 URL을 변경
    template_name = 'accounts/form.html',
    #로그인 성공했을 때 보낼 URL
    success_url = settings.LOGIN_URL,
)

login = LoginView.as_view(
    template_name = 'accounts/form.html',
)

logout = LogoutView.as_view(
    next_page = settings.LOGIN_URL,
)


# 로그인 된 경우만 아래 함수가 실행될 수 있도록 함
# 로그인 하지 않은 상태로 아래 함수를 호출하게 되면 해당 유저는 로그인 화면으로 가게된다
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')