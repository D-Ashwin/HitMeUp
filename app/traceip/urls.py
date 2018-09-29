from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^trace/', views.traceipfromget,name = 'traceip'),
]