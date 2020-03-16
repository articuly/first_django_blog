from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm


# 通过自写视图函数实现登陆
def user_login_view(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'account/login.html', {'form': login_form})
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse('Welcome you. You have logined the website.')
            else:
                return HttpResponse('Sorry, your username or password is not correct.')
        else:
            return HttpResponse('Invalid login.')


def register(request):
    if request.method == 'GET':
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()  # 补充一个表
        return render(request, 'account/register.html', {'form': user_form, 'profile': userprofile_form})
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid():  # 相当于and逻辑
            new_user = user_form.save(commit=False)  # 获验证后的表单，创立对象但不提交
            new_user.set_password(user_form.cleaned_data['password'])  # 设定用户密码
            new_user.save()  # 最后保存注册的用户
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user  # 模型里User UserProfile字段对应
            new_profile.save()
            return HttpResponse('恭喜，注册成功了。')
        else:
            return HttpResponse('对不起，注册失败了。')
