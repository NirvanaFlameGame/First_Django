from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>:<i>Румянцев Ю.А. </i>
    """
    return HttpResponse(text)
