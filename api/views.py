from .models import Users
from .serializers import UsersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status

# Create your views here.


@api_view(["GET", "POST"])
def user_retrieve_info_admin(request):
    # [GET] /api/users/ List all the users for the user organization if user is `Administrator` or `Viewer`. Must return all the user model fields. Should support search by name, email. Should support filter by phone.

    if request.method == "GET":
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    # POST /api/users/ Create an user for the organization, must set password as well. Request user must be Administrator
    if request.method == "POST":
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
