from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def num(request):
    if request.method == 'POST':
        # Obtener los números del cuerpo de la solicitud POST
        number1 = int(request.POST.get('num1', 0))
        number2 = int(request.POST.get('num2', 0))
        number3 = int(request.POST.get('num3', 0))
        
        total = number1 + number2 + number3
        if total > 50:
            return HttpResponse(f'La suma es: {total}')
        else:
            return HttpResponse(f'Haz realziado la prueba: {total}')
    return render(request, 'ap.html')