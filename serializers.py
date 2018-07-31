from .models import description
from rest_framework import serializers

class descriptionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=description
		fields=('url' ,'book_name','book_price','book_author')