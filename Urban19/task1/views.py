from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


# Create your views here.
def main_page(request):
    return render(request, 'menu.html')


def shop_page(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'shop.html', context)


def cart_page(request):
    return render(request, 'cart.html')



# def sign_up_by_html(request):
#     users = Buyer.objects.all()
#     info = {}
#     context = {
#         'info': info,
#         'users': users
#     }
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = hash(request.POST.get('password'))
#         repeat_password = hash(request.POST.get('repeat_password'))
#         age = int(request.POST.get('age'))
#
#         if password == repeat_password and age >= 18 and username not in users:
#             Buyer.objects.create(username=username, password=password, age=age)
#             return HttpResponse(f"Приветствуем, {username}")
#
#         elif password != repeat_password:
#             info['error'] = 'Пароли не совпадают'
#
#         elif age < 18:
#             info['error'] = 'Вы должны быть старше 18'
#
#         elif username in users:
#             info['error'] = 'Пользователь уже существует'
#
#     if info.get('error') is not None:
#         return HttpResponse(info["error"])
#
#     return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    context = {
        'info': info,
        'users': users
    }
    if request.method == 'POST':
        all_usernames = []
        for user in users:
            all_usernames.append(user.username)

        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            context['form'] = form

            if password == repeat_password and int(age) >= 18 and username not in all_usernames:
                Buyer.objects.create(username=username, password=password, age=age)
                return HttpResponse(f"Приветствуем, {username}")

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

            elif username in all_usernames:
                info['error'] = 'Пользователь уже существует'

        if info.get('error') is not None:
            return HttpResponse(info["error"])

    else:
        form = UserRegister()
        context['form'] = form

    return render(request, 'registration_page.html', context)
