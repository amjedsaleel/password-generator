from django.shortcuts import render
from . import alpha

# Create your views here.


def index(request):
    if request.method == "POST":
        password_length = request.POST.get('password-length')
        print(password_length)

        gen = alpha.generate(int(password_length))
        print(gen)

    context = {}
    return render(request, 'index.html', context)


