from django.urls import path
from upload import upload

urlpatterns = [
    # 副路由表
    path('upload_head/', upload.upload_head),
    path('upload_image/', upload.upload_image)
]
