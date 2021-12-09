from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    url(r'^api/odebrecht/professional$', views.professional_list),
    url(r'^api/odebrecht/professional/(?P<pk>[0-9]+)$', views.professional_detail),
]