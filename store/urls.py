from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.index, name='home'),
    path('categories/<int:cat_id>/', views.categories, name='cats_id'),
    path('about/', views.about, name='about'),
    path('warranty/', views.warranty, name='warranty'),
    path('delivery/', views.delivery, name='delivery'),
    path('contacts/', views.contacts, name='contacts'),
    path('gpu/', views.gpu, name='gpu'),
    path('cpu/', views.cpus, name='cpu'),
    path('cooler/', views.cooler, name='cooler'),
    path('memory/', views.memory, name='memory'),
    path('psu/', views.psu, name='psu'),
    path('case/', views.case, name='case'),
    path('motherboard/', views.motherboard, name='motherboard'),
    path('ram/', views.ram, name='ram'),
    path('search/', views.search_products, name='search'),
    path('<str:component>/<int:pk>/', views.component_detail, name='component_detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)