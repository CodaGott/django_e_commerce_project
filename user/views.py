from django.shortcuts import render


def create_user(request):
    return render(request, '../templates/user/create_user_page.html')


def user_page(request):
    return render(request, '../templates/user/user_page.html')
