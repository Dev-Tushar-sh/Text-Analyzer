from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index ,name = 'index'),
    path('index/',views.index ,name = 'index'),
    path('removepunc/', views.removepunc ,name = 'RmvPunc'),
    path('capatalize/', views.capatalizefirst ,name = 'CPFirst'),
    path('newlineremove/', views.newlineremove ,name = 'NLR'),
    path('spaceremover/', views.spaceremover ,name = 'SpcRmv'),
    path('charcount/', views.charcount ,name = 'ChCo'),
    path('result/', views.result ,name = 'RS')
]
