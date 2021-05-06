from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogComment
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    path('post/new/', BlogCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name = 'post_delete'),
    path('post/<int:pk>/comment', login_required(login_url = 'login')(BlogComment.as_view()), name = 'post_comment'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
]