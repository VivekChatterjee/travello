from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from travello import views as tv

urlpatterns = [
    path('', include('travello.urls')),
    # path('', views.index),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # path('', views.home),
    path('about/', views.about),

    # int
    # path('about/<int:id>', views.aboutYou),
    # string
    # path('about/<str:id>', views.aboutYou),
    # slug (how-to-browse-web)
    # path('about/<slug:id>', views.aboutYou),

    # any type
    path('about/<id>', views.aboutYou),
    path('add/', views.add),

    # api calls
    path('destination_details/<int:pk>', tv.destination_details),
    path('destinations/', tv.destinations)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
