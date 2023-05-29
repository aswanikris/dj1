from django.urls import path
from app3 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.fun,name='fun'),
    path('update/<int:todo_id>/',views.update,name='update'),
    path('delete/<int:todo_id>/',views.delete,name='delete'),
  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)