from rest_framework import routers
from items.views import ItemViewSet

router = routers.DefaultRouter()

router.register(r'item', ItemViewSet)
