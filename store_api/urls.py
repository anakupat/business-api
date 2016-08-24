from django.conf.urls import url
from rest_framework import routers
from store_api.views import IncomeViewSet

router = routers.DefaultRouter()
router.register(r'incomes', IncomeViewSet)

urlpatterns = router.urls