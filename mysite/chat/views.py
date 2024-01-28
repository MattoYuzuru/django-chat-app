from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse


@login_required
def chatPage(request, *args, **kwargs):
    context = {}
    return render(request, "chat/chatPage.html", context)


def checkTest(request):
    return render(request, "chat/navbar.html", {})


def my_ajax_view(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        field1_value = request.POST.get('field1')
        data = {
            'message': 'Данные успешно отправлены!'
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Недопустимый запрос'})
