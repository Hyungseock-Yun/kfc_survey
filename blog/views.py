from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Admin
from kfc_survey.survey_test import survey_start


def posts(request):
    ## published_at 컬럼이 null이 아닐 경우, 데이터를 내림차순(order by) 정렬하여 가져온다.
    posts = Admin.objects.filter(created_at__isnull=False).order_by('-created_at')

    ## 가져온 데이터를 blog/posts.html 페이지에 posts라는 key값으로 전달
    return render(request, 'blog/survey.html', {})


def post_detail(request, id):
    post = get_object_or_404(Admin, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        select_user_info(username)
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'survey.html')
        else:
            return render(request, 'main.html', {'error': 'username or password is incorrect'})


def select_user_info(userID):
    admin = Admin.objects.get(username=userID)
    print(admin)


def survey(request):
    if request.method == "POST":
        number = request.POST['number']
        print('views number : ' + number)
        result = str(survey_start(number))
        print('result : ' + result)

        return render(request, 'blog/survey.html', {'status': result})