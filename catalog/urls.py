from django.urls import path
from catalog.apps import CatalogConfig
# from catalog.views import products_list, products_detail
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

# urlpatterns = [
#     path("", products_list, name='products_list'),
#     path("products/<int:pk>/", products_detail, name='products_detail')
# ]


urlpatterns = [
    path("", ProductListView.as_view(), name='products_list'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name='products_detail'),
    path("products/create", ProductCreateView.as_view(), name="products_create"),
    path("products/<int:pk>/update", ProductUpdateView.as_view(), name="products_update"),
    path("products/<int:pk>/delete", ProductDeleteView.as_view(), name="products_delete")
]
