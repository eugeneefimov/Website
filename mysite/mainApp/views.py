from django.shortcuts import render



def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Еcть вопросы?', '8 956 753 12 25',
                                                             'ram@mail.ru']})


def media(request):

    return render(request, request.POST)
