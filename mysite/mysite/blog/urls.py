from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # Commenting the old path to PostDetail views before making it a function: path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail' ),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]