from django.shortcuts import render
from django.http import HttpResponse
from .models import registration

# def members(request):
#     return HttpResponse("Hello World")

def register(request):  
    # erros = ''
    if request.method == 'POST':
        print(request.POST)
        ism_falmilya = request.POST.get('ism_falmilya')
        yosh = request.POST.get('yosh')
        telfon_nomer = request.POST.get('telfon_nomer')
        radio = request.POST.get('radio')
        email = request.POST.get('email')

        # if pasword != paswrod2:
        #     erros ['msg'] = 'your pasward is not same'

        # gjango ORM code for add database
        registration.objects.create(

            ism_falmilya = ism_falmilya,
            yosh = yosh,
            telfon_nomer = telfon_nomer,
            radio = radio,
            email = email
        )
        return HttpResponse('Congritulation you rregistered')

    return render(request, 'index.html')     #{'erros': error}
    










