from django.urls import path
from . import views
urlpatterns = [
    path('', views.todo_home, name="todo_home"),
    path('/delete/<list_id>', views.delete, name="delete"),
    path('/cross_off/<list_id>', views.cross_off, name="cross_off"),
    path('/cross_on/<list_id>', views.cross_on, name="uncross"),
    path('/todo_api_home', views.api_view, name="api_view"),

]