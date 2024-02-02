from django.contrib import admin
from django.urls import path

import tutor.views as tutor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', tutor.gpt_form),
]