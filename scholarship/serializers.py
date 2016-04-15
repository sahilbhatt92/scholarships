from rest_framework import serializers
from models import Scholarships

class ScholarshipSerializer(serializers.ModelSerializer):
	class Meta:
		model = Scholarships
		fields = ('id', 'name', 'about', 'end_date', 'amount', 'amount_type', 'created')
