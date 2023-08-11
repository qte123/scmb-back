from django.urls import path
from images import images

urlpatterns = [
    # 副路由表
    path('do/', images.dispatcher)
]
