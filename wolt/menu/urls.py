from django.urls import path
#from some_app.views import AboutView
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    #path('about/', TemplateView.as_view(template_name="polls/game_aalto.html")),
    #path('game/<str:gameid>', views.AboutView.as_view(), name='game'),
    path('list/', views.AboutView.as_view(), name='about'),
    path('A-Z/', views.AlphabetView.as_view(), name='az'),
    path('Z-A/', views.ZalphabetView.as_view(), name='za'),
]
