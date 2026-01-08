from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('book_detail/', views.book_detail, name="book_detail"),
    path('liste_book/', views.liste_book, name="liste_book"),
    path('menu-item/<int:pk>/', views.display_menu_item, name='menu_item'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),

    # API
    path('api/menu/', views.MenuListCreateView.as_view()),
    path('api/menu/<int:pk>/', views.MenuDetailView.as_view()),
    path('api/bookings/', views.BookingListCreateView.as_view()),
    path('api/register/', views.RegisterView.as_view()),

]
