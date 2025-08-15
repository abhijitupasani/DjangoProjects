from rest_framework import serializers
from .models import Book, Publisher

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'cover', 'created_by', 'publisher']
        read_only_fields = ['created_by']  
        
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)    
    
    def get_publisher_name(self, obj):
        return obj.publisher.name if obj.publisher else None
    
    def validate_title(self, value):
        if 'harry' not in value.lower():
            raise serializers.ValidationError("Title must contain 'Harry'")
        return value
    
class BookHyperlinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'title', 'publisher']
        extra_kwargs = {
            'url': {'view_name': 'book-detail', 'lookup_field': 'id'}
        }