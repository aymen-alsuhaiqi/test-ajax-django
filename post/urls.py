from django.urls import path

from . import views
urlpatterns = [
        path('', views.index, name='index'),  # index view at /
        path('posts', views.getPosts, name='get_posts'),  # index view at /
        path('likepost', views.likePost, name='likepost'),   # likepost view at /likepost
        path('submit/', views.post_posts, name='submit_post'),
        path('detail/<int:p_id>', views.post_detail, name='detail'),
        path('delete/<int:p_id>', views.delete, name='delete'),

   ]