from django.urls import path
from . import views
from .views import UserEditView, PasswrodsChangeView, AddCommentView
 
urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
    path('drafts/', views.post_draft_list, name = 'post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name = 'register'),
    path('add_category/', views.AddCategoryView, name = 'add_category'),
    path('category/<str:cats>/', views.category_views, name = 'category'),
    path('like/<int:pk>', views.LikeView, name = 'like_post'),
    path('edit_profile/', UserEditView.as_view(), name = 'edit_profile'),
    path('password/', PasswrodsChangeView.as_view(template_name='change-password.html')),
    path('password_success', views.password_success, name = 'password_success'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name = 'add_comment'),
]