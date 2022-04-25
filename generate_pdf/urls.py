from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('generate_document/', views.generate_document, name="generate_document"),
    path('get_document/', views.getPdfPage, name="get_document"),
    path('test/', views.pdf, name="pdf")

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
