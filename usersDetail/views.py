# IMPORT LIBRARIES
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import AuthenticationFailed
from .models import usersDetail
from .serializers import UserDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
import os
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDetailSerializer

@api_view(['POST'])
@permission_classes([])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.status == 'APPROVED':
                    refresh = RefreshToken.for_user(user)
                    access_token = str(refresh.access_token)
                    refresh_token = str(refresh)
                    return JsonResponse({
                        'message': 'User authenticated successfully',
                        'token': access_token,
                        'refresh_token': refresh_token,
                        'user': {
                            'id': user.id,
                            'email': user.email,
                            'first_name': user.first_name,
                            'last_name': user.last_name,
                            'birthday': user.birthday,
                            'gender': user.gender,
                            'mobile': user.mobile,
                            'region': user.region,
                            'zone': user.zone,
                            'kebele': user.kebele,
                            'organization': user.organization,
                            'status': user.status,
                            'role': user.role
                        }
                    })
                else:
                    return JsonResponse({'message': 'User not approved'}, status=403)
            else:
                return JsonResponse({'message': 'Invalid email or password'}, status=400)
        else:
            return JsonResponse({'message': 'Email or password is missing'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

# UPLOAD IMAGES
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_files(request):
    uploaded_files = request.FILES.getlist('files')
    file_urls = []
    for uploaded_file in uploaded_files:
        file_path = os.path.join(settings.MEDIA_ROOT_PROFILE, uploaded_file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        file_urls.append(file_path)
    return Response({'file_urls': file_urls})

# FETCH USERS 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_users_api(request):
    users = usersDetail.objects.all()
    serializer = UserDetailSerializer(users, many=True)
    return Response(serializer.data)

# FETCH USER
@api_view(['GET'])
@permission_classes([])
def fetch_user_api(request, pk):
    user = usersDetail.objects.get(pk=pk)
    serializer = UserDetailSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_api(request):
    data = request.data.copy()  
    password = data.get('password')
    if not password:
        return Response({"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserDetailSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()  
        user.set_password(password)  
        user.save()  
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_api(request, pk):
    try:
        user = usersDetail.objects.get(pk=pk)
    except usersDetail.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    data = request.data.copy()
    password = data.pop('password', None)  # Remove password from data to handle separately
    
    serializer = UserDetailSerializer(user, data=data, partial=True)  # Allow partial updates
    if serializer.is_valid():
        if password:  # Encrypt the password if provided
            user.set_password(password)
        serializer.save()  # Save other fields
        user.save()  # Save the user to persist the password change if applicable
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# DELETE USER
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_api(request, pk):
    user = usersDetail.objects.get(pk=pk)
    user.delete()
    return Response(status=204)




# BLOCK THE USER
@api_view(['PATCH'])
@permission_classes([])
def block_user_api(request, pk):
    try:
        user = usersDetail.objects.get(pk=pk)
        user.status = 'BLOCKED'
        user.save()
        return Response(status=204)
    except usersDetail.DoesNotExist:
        return Response(status=404)


# APPROVE THE USER
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def approve_user_api(request, pk):
    try:
        user = usersDetail.objects.get(pk=pk)
        user.status = 'APPROVED'
        user.save()
        return Response(status=204)
    except usersDetail.DoesNotExist:
        return Response(status=404)

@api_view(['POST'])
@permission_classes([])
def refresh_token(request):
    if 'refresh_token' in request.data:
        refresh_token_str = request.data['refresh_token']
        try:
            refresh = RefreshToken(refresh_token_str)
            new_access_token = str(refresh.access_token)

            return JsonResponse({
                'access_token': new_access_token
            })
        except Exception as e:
            return JsonResponse({'error': 'Invalid refresh token'}, status=400)
    else:
        return JsonResponse({'error': 'Refresh token not provided'}, status=400)
