from django.urls import path

from . import views

urlpatterns = [
    # blank string at the end of path. end of url. ex: /madlibs/
    path('', views.index, name='index'),
    # This is a detail view,added to make the program work, but should be removed or altered later
    # path('<int:entry_id>/', views.detail, name='detail'),
    # ex: madlibs/3/
    path("<int:entry_id>/", views.input, name='input'),  # This one should lead to a template in views
    # ex: /madlibs/3/results/  it is possible the /3 is unneeded
    path("<int:entry_id>/results/", views.results, name='results'),
    # if results is for multiple items instead of just one item, uncomment the line below and comment the above line
    # path("results/", views.results, name='results')
    

]