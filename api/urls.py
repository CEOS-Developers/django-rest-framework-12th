#from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from . import views

#create a router and register our viewsets with it
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'choices', views.ChoiceViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'carts', views.CartViewSet)

#The API URLs are now determined automatically by the router
urlpatterns = router.urls



#urlpatterns = format_suffix_patterns(urlpatterns)


