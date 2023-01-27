############ class based view ##############
from rest_framework.response import Response
from rest_framework import status
from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework.views import APIView



class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
        # context={'request': request}
        return Response(serializer.data)



    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class StreamPlatformDetail(APIView):
    def get(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



class WatchListAV(APIView):
    def get(self, request):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

class WatchDetail(APIView):
    def get(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)












############ function based view ##############
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from watchlist_app.models import Movie
# from watchlist_app.api.serializers import MovieSerializer


# @api_view(['GET','POST'])
# def movie_list(request):
#     if (request.method=='GET'):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if (request.method=='POST'):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

# @api_view(['GET','DELETE','PUT'])
# def movie_details(request,pk):
#     if (request.method=='GET'):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if (request.method=='DELETE'):
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     if (request.method=='PUT'):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

