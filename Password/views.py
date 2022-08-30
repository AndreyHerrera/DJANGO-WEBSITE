from django.shortcuts import render
import random

def password_generator(request):
    characters= list('abcdefghijklpoqrstvwxyz')
    default_length = 0
    
    if request.GET.get('length'):
        default_length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLPOQRSTVWXYZ'))

    if request.GET.get('symbols'):
        characters.extend(list('!@#$%&*^'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    generated_password = ''

    for x in range(default_length):
        if default_length >= 8 and default_length <=16:
            generated_password += random.choice(characters)

        else:
            generated_password == ''

    return render(request, 'password.html', {'password' : generated_password})