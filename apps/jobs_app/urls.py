from django.urls import path
from . import views

urlpatterns = [
    path('jobs/home', views.home),
    path('logout', views.logout),
    path('jobs/new', views.new),
    path('jobs/add_new', views.add_new),
    path('add_job/<int:id>',views.add_job),
    path('remove/<int:id>',views.remove_job),
    path('jobs/<int:id>', views.job_info),
    path('give_up/<int:id>', views.give_up),
    path('done/<int:id>', views.done),
    path('jobs/edit/<int:id>', views.edit),
    path('edit_job/<int:id>', views.edit_job)
    
]