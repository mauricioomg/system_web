from django.urls import path
from . import views


app_name = 'index'
urlpatterns = [
    # LANDING
    path('', views.IndexView.as_view(), name='index'),
    path('about-us', views.AboutUsView.as_view(), name='about_us'),
    # END_LANDING
    # USERS
    path('user/register/', views.UserRegisterView.as_view(), name='user_register'),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('user/login/', views.UserLoginView.as_view(), name='user_login'),
    path('user/logout/', views.UserLogoutView.as_view(), name='user_logout'),
    # END_USERS
    # BOOKS
    path('list/books/', views.ListBooksView.as_view(), name='list_books'),
    path('book/<int:pk>/detail', views.DetailBookView.as_view(), name='detail_book'),

    path('list/my-books/', views.ListMyBooksView.as_view(), name='list_my_books'),
    path('create/book/', views.CreateBookView.as_view(), name='create_book'),
    path('update/<int:pk>/book/', views.UpdateBookView.as_view(), name='update_book'),
    path('book/<int:pk>/delete', views.DeleteBookView.as_view(), name='delete_book'),
    # END_BOOKS
]
