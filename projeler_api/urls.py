from django.urls import path,include

from rest_framework.routers import DefaultRouter

from projeler_api import views

router = DefaultRouter()
router.register('project',views.ProjeViewSet)
router.register('personel',views.PersonelListViewSet)



urlpatterns = [
    path('',include(router.urls))
]