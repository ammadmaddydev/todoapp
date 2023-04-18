from django.urls import path
from users_todo.views import home, login, signup, createAccount, loginAccount, logoutAccount, AddNewTodo, markCompleted,enablePriority, deleteTodo, disablePriority


urlpatterns=[
    path('', home, name='home'),
    path('login/', login, name='login_view'),
    path('signup/', signup, name='signup_view'),
    path('create_account/', createAccount, name='create_account'),
    path('login_account/', loginAccount, name='login_account'),
    path('logout_account/', logoutAccount, name='logout_account'),

    path('add_new_todo/', AddNewTodo, name='add_new_todo'),
    path('mark_complete/<int:todo_id>', markCompleted, name='mark_complete'),
    path('enale_priority/<int:todo_id>', enablePriority, name='enale_priority'),
    path('disable_priority/<int:todo_id>', disablePriority, name='disable_priority'),
    path('delete_todo/<int:todo_id>', deleteTodo, name='delete_todo'),
]