from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product-read', ProductReadOnlyModelViewSet, basename='product-read')
router.register(r'product', ProductViewSet)


urlpatterns = router.urls