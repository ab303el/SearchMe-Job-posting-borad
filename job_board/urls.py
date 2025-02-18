from django.urls import path
from .views import index , detail , main
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/<int:pk>',index , name = 'index'),
    path('detail/<int:pk>/', detail , name= 'detail'),
    path('' , main , name='main' )
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)