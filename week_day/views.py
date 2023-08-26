from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def weekdayView(request):
    return HttpResponse('Dushanba, Seshanba, chorshanba, Payshanba, Juma, Shanba, Yakshanba')
def weekday1View(request):
    return HttpResponse('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday')
def weekday2View(request):
    return HttpResponse('Понедельник, вторник, среда, Четверг, Пятница, Суббота, воскресенье')