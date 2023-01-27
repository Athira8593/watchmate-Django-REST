from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchDetail, StreamPlatformAV,StreamPlatformDetail

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetail.as_view(), name='watch-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-platform'),
    path('stream/<int:pk>/', StreamPlatformDetail.as_view(), name='streamplatform-detail'),
]


####### function based view ##########
# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('<int:pk>/', movie_details, name='movie_detail'),
# ]