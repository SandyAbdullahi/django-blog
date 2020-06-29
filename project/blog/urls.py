from django.urls import path

from . import views

urlpatterns = [
    path('post/<int:post_id>/delete', views.delete_post),
    path('post/<int:post_id>/update', views.update_post),
    path('post/<int:post_id>/', views.post_view),
    path('new_post/', views.new_post, name="new_post"),
    path('about/', views.about, name='about'),
    path('', views.home, name="home")
]
