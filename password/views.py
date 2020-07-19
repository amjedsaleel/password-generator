from django.shortcuts import render
from .alpha import generate

# Create your views here.


def index(request):
    generated_password = ''
    if request.method == "POST":
        password_length = int(request.POST.get('password-length'))
        generated_password = generate(password_length)

        print(generated_password)

    context = {'password': generated_password}
    return render(request, 'index.html', context)
