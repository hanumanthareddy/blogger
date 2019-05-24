from django.urls import path

from .views import PostsView, PostDetailedView, PostNew, PostUpdate, PostDelete

urlpatterns = [
    path('', PostsView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailedView.as_view(), name='post_detail_view'),
    path('post/new/', PostNew.as_view(), name='PostNew'),
    path('post/<int:pk>/edit/', PostUpdate.as_view(), name='PostUpdate'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='PostDelete')
]
