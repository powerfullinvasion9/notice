from django.urls import path
from .views import *

urlpatterns = [
    path('', NoteHome.as_view(), name='home'),
    path('add/', AddNoteView.as_view(), name='adding_page'),
    path('<int:pk>/', NoteDetailView.as_view(), name='detail_page'),
    path('register/', registration, name='register_page'),
    path('login/', loginPage, name='login_page'),
    path('logout/', logoutUser, name='logout_page')
]