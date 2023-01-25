from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetail, StreamPlatform

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetail.as_view(), name='movie_detail'),
    # path('stream/', StreamPlatform.as_view(), name='stream-platform'),
]


####### function based view ##########
# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('<int:pk>/', movie_details, name='movie_detail'),
# ]