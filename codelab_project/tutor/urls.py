from django.contrib import admin
from django.urls import path

import tutor.views as tutor

urlpatterns = [
    path('hello/', tutor.gpt_form),
]