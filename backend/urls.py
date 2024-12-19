
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('usersDetail.urls')),
    path('api/poultry/', include('poultry.urls'))  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

