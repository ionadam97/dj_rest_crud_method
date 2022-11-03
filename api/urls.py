from django.urls import path, include
from . import views




urlpatterns = [ 
    # viewset
    path('api/', include('api.routers')),  

    # generics urls
    path('product-create/', views.ProductCreateAPIView.as_view()),
    path('product-list/', views.ProductListAPIView.as_view()),
    path('product-retrive/<int:pk>/', views.ProductRetrieveAPIView.as_view()),
    path('product-destroy/<int:pk>/', views.ProductDestroyAPIView.as_view()),
    path('product-update/<int:pk>/', views.ProductUpdateAPIView.as_view()),
    path('product-list-create/', views.ProductListCreateAPIView.as_view()),
    path('product-retrive-update/<int:pk>/', views.ProductRetrieveUpdateAPIView.as_view()),
    path('product-retrive-destroy/<int:pk>/', views.ProductRetrieveDestroyAPIView.as_view()),
    path('product-retrive-update-destroy/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view()),



    # APIView
    path("product/", views.ProductList.as_view()),      
    path("product/<int:pk>/", views.ProductDetail.as_view()), 

]

