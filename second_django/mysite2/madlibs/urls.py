from django.urls import path

from . import views


app_name = 'madlibs'
urlpatterns = [
    # index page. ex: madlibs/
    path('', views.index, name='index'),
    # Input page. ex: madlibs/1/input
    path('<int:master_id>/input', views.input, name='input'),
    # Results page. ex: madlibs/1/results
    path('<int:master_id>/results', views.results, name="results"),
]