from django.conf import settings

from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib import admin
from AppComponent1 import views
from .views import SignupView

urlpatterns = [
    path("", TemplateView.as_view(template_name="homepage.html"), name="home"),
    path("admin/", admin.site.urls),
    path("account/signup/",SignupView.as_view(),name="account_signup"),
    path("account/", include("account.urls")),
    path('AppComponent1/',include('AppComponent1.urls')),
    path("AppComp/gotothis",views.CseView),
    path('AppComp/CountView/<slug:slug>/',views.CountView),
    path('AppComp/CountViews/<slug:slug>/',views.CountViews),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
