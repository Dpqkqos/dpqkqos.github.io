from django.urls import path
from . import views

urlpatterns = [
    path('user-state/<str:chat_id>/', views.user_state, name='user_state'),
    path('save-state', views.save_state, name='save_state')
]