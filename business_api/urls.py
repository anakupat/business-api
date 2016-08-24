from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('store_api.urls', namespace='store api')),
    url(r'^api-auth/', include('rest_framework.urls')), # Add login to api
    url(r'^admin/', admin.site.urls),
]
