from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform, Reviews

# model serializer


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        # fields = '__all__'
        exclude = ['watch_list']

        
        
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True) # mention as related name in models
    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['id','active']


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'



















# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name =serializers.CharField(validators=[name_legth])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#     def update(self,instance,validated_data):
#             instance.name = validated_data.get('name', instance.name)
#             instance.description = validated_data.get('description', instance.description)
#             instance.save()
#             return instance
        
#     # # field level validation
#     def validate_description(self, value):
#         if len(value)<2:
#             raise serializers.ValidationError("description is too short")
#         else:
#             return value
    
#     # object level validation
#     def validate(self, data):
#         if data['name']== data['description']:
#             raise serializers.ValidationError("description is not eqaul to name")
#         else:
#             return data
