
from django.urls import path
from web.home import views
from web.web.urls import urlpatterns

urlpatterns = [
    path('hello_world/', views.hello_world)
]