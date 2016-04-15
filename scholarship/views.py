from serializers import ScholarshipSerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from models import Scholarships


@api_view(['GET', 'POST'])
def scholarship_list(request):
	"""
	Function: scholarship_list(RequestData)
	-- GET Method: 
		Returns: all list of scholarships
	-- POST Method: 
		Accepts: data as Json to add new scholarship
		Returns: scholarship data after creation of scholarship
	"""

	if request.method == "GET":
		scholarships = Scholarships.objects.all()
		serializers = ScholarshipSerializer(scholarships, many=True)
		return Response(serializers.data, status=status.HTTP_200_OK)

	elif request.method == "POST":
		serializers = ScholarshipSerializer(data=request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data, status=status.HTTP_201_CREATED)
		return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def scholarship_details(request, pk):

	"""
	Function: scholarship_details(RequestData, PrimaryKey)
	-- GET Method: 
		Returns: a scholarship
	"""

	try:
		scholarship = Scholarships.objects.filter(pk=pk)
	except Scholarships.DoesNotExist:
		return Http404

	if request.method == "GET":
		serializers = ScholarshipSerializer(scholarship, many=True)
		return Response(serializers.data)


