from django.urls import path
from .views import home, form, post_list_id, post_list_slug, post_detail_with_id, post_detail_with_slug , post_delete_id , update_post_id
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('post-list-id/', post_list_id, name='post_list_id'),
    path('post-list-slug/', post_list_slug, name='post_list_slug'),
    path('post-detail/<uuid:id>/', post_detail_with_id, name='post_detail_id'),
    path('post-detail/<slug:slug>/', post_detail_with_slug, name='post_detail_slug'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('post-delete/<uuid:id>/', post_delete_id, name='post_delete_id'),
    path('post-update/<uuid:id>/', update_post_id, name='post_update_id'),
]