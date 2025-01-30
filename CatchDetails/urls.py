from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('catch', views.submit_a_catch, name="catch"),
    # path('submit', views.submit, name="submit"),
    # path('catchinitial', views.catch, name="catch"),
    path("load_subspecies", views.load_subspecies, name="load_subspecies"),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)