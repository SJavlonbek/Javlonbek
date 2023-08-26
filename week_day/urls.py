from django.urls import path
from .views import weekdayView
from .views import weekday1View
from .views import weekday2View

urlpatterns = {
    path('weekdays/uz', weekdayView, name='weekdays'),
    path('weekdays/en', weekday1View, name='weekdays1'),
    path('weekdays/ru', weekday2View, name='weekdays2')
}