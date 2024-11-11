from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("loginn/", views.loginn, name="login"),
    path("todo/", views.todo, name="todo"),
    path("edit_todo/<int:srno>", views.edit_todo, name="edit_todo"),
]
