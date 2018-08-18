from api import views
from rest_framework.routers import DefaultRouter
from django.urls import include, path
router = DefaultRouter()

router.register('user', views.UserViewset)

urlpatterns = router.urls