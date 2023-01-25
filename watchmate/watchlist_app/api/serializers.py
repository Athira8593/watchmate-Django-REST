from rest_framework import serializers
from watchlist_app.models import Movie

# model serializer

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['id','active']

    # # field level validation
    def validate_description(self, value):
        if len(value)<2:
            raise serializers.ValidationError("description is too short")
        else:
            return value
    
    # object level validation
    def validate(self, data):
        if data['name']== data['description']:
            raise serializers.ValidationError("description is not eqaul to name")
        else:
            return data





# def name_legth(value):
#     if len(value)<2:
#         raise serializers.ValidationError("name is too short")
#     else:
        
#         return value
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
