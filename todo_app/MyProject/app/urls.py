from django.urls import path

from app.views import TodoListApiView, TodoDetailApiView

urlpatterns = [
        path('todo', TodoListApiView.as_view()),
        path('todo/<int:id>', TodoDetailApiView.as_view()),
]