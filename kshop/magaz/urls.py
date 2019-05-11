from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *
from magaz import views
from kshop import settings
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter
e_router=ExtendedSimpleRouter()
(
    e_router.register(r'category',CategoryView,base_name='category')
            .register(r'products',ProductFilterView,base_name='category-products',
                      parents_query_lookups=['category_products']
                      )
)


router = routers.DefaultRouter()
router.register(r'available', views.ProductIsAvailable)
router.register(r'seil',views.ProductSeil)
router.register(r'product',views.ProductSum)


urlpatterns = [
    url(r'^',include(router.urls)),
    url(r'^',include(e_router.urls)),
    url(r'order', OrderAPIView.as_view()),
    url(r'bill', BillAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)