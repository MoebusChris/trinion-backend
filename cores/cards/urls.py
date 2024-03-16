from rest_framework.routers import SimpleRouter

from .views.card import CardViewSet

router = SimpleRouter(trailing_slash=False)
router.register('cards', CardViewSet)

urlpatterns = router.urls
