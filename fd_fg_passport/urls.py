"""
URL configuration for fd_fg_passport project.

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core.views import (
    LandingView, 
    MO_City_View,
    MO_View,
    RegionReport,
    ReviewView,
    ReviewCreateView,
    ReviewAnswerCreateView,
    importView,
    NewLogoutView,
    NewLoginView,
    RegisterView,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingView.as_view(), name='landing'),    
    path('mo/<int:mo_id>/', MO_View.as_view(), name='mo'), 
    path('mo_city/<int:mo_id>/', MO_City_View.as_view(), name='mo_city'),
    path('regionreport/', RegionReport.as_view(), name='regionreport'), 
    path('reviews/', ReviewView.as_view(), name='reviews'), 
    path("reviews/create/", ReviewCreateView.as_view(), name="review_create"),
    path("answer/create/<int:pk>/", ReviewAnswerCreateView.as_view(), name="answer_create"),
    path('import/', importView.as_view(), name='import'), 
    path("logout/", NewLogoutView.as_view(), name="logout"), 
    path("register/", RegisterView.as_view(), name="register"),  
    path("login/", NewLoginView.as_view(), name="login"),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)