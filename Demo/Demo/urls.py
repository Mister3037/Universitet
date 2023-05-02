
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('', bosh_sahifa),
    path('kitoblarim', mening_kitoblarim),
    path('studentlar', talabalar),
    path('bitiruvchilar', bitiruvchi_talaba),
    path('talaba/<int:son>/', bitta_talaba),
    path('shahar', shahar),
    path('malumot', ism),
]
