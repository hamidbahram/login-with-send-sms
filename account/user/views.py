from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import render
from .models import profile
from random import randint
from kavenegar import *
import requests


@csrf_exempt
def get_code(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        code = randint(1000, 9999)
        str_code = str(code)
        code_active = profile.objects.get_or_create(
            username=phone, active_code=code)
        api = KavenegarAPI(
            'API_KEY')
        params = {
            'sender': '1000596446',
            'receptor': phone,
            'message': str_code}
        response = api.sms_send(params)
        return JsonResponse({"response": response})


@csrf_exempt
def chek_code(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        code = request.POST.get('code')
        try:
            prof = profile.objects.get(username=phone)
            if int(code) == prof.active_code:
                return HttpResponse('login')
            else:
                return HttpResponse('invalid code')
        except:
            pass
        pass


# @csrf_exempt
# def get_code(request):
#     # if request.method == 'POST':
#         to = request.GET.get('phone')
#         code = str(randint(1000, 9999))
#         API_key = "6A636F7351374241713478713043625A477378364A556A2B4A4F466E5A46354D693241463570384F3041493D"
#         url = "https://api.kavenegar.com/v1/%s/sms/send.json" % API_key
#         payload = {'receptor': to, 'message': code}
#         response = requests.post(url, data=payload)
#         return HttpResponse(response)
