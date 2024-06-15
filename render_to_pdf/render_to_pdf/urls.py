from django.contrib import admin
from django.urls import path
from .views import GeneratePDF

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdf/', GeneratePDF.as_view())
]
