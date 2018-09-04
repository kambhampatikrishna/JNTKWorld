from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 
from . import views
urlpatterns = [
    path('gotothis/',views.CseView),
    path('into',views.storetodb,name='storetodb'),
    path('storetodb2',views.storetodb2,name='storetodb2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)