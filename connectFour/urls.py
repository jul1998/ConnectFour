from django.urls import path

from . import views

urlpatterns = [
    path('', views.start_game, name='start_game'),
    path('make_move', views.make_move, name='make_move'),
    path('get_game_data/<int:game_id>', views.get_game_data, name='get_game_data'),
]