from django.http import HttpResponse
# Create your views here.
def weekday1View(request):
    return HttpResponse('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday')
