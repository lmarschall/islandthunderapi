from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate

from rest_framework import viewsets
from rest_framework import views
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

import binascii
import os

from .models import Player
# from .serializers import PlayerSerializer
# from rest_framework.authtoken.models import Token

import json

# Create your views here.

# api endpoint for the user to generate authentication token
@api_view(["POST"])
# @permission_classes((AllowAny,))
def auth(request):

    # # get the steam uid
    uid = request.data.get("uid")

    if uid is None:
        return Response({'error': 'Please provide uid'}, status=HTTP_400_BAD_REQUEST)

    # TODO token framework implementation
    # player = authenticate(request)

    # search for steam uid in database
    try:
        player = Player.objects.get(uid=uid) # get the player
    # except User.DoesNotExist:
    except:
        # no player found create new player
        player = Player.objects.create(uid=uid)

    # calculate the auth token
    token = binascii.hexlify(os.urandom(20)).decode()

    # save auth token to player
    player.token = token
    player.save()

    # TODO token framework implementation
    # token, created = Token.objects.get_or_create(user=data)
    # print(token.key)

    return Response({"auth_token": token})

# api endpoint for the server to check authentication token and generate bearer token
@api_view(["POST"])
def check(request):

    # get uid and auth token from request
    uid = request.data.get("uid")
    token = request.data.get("token")

    # search for steam uid in database
    try:
        player = Player.objects.get(uid=uid, token=token) # get the player
    # except User.DoesNotExist:
    except:
        # player with given uid and token not found, return error
        return Response({'error': 'Player with given uid and token not found'}, status=HTTP_400_BAD_REQUEST)

    # set the player as authorized
    player.authorized = True

    # create access token
    token = binascii.hexlify(os.urandom(20)).decode()
    player.token = token

    # save player
    player.save()

    return Response({"access_token": token})


# api endpoint for user to access saved informations
@api_view(["GET"])
def user(request):

    token = request.headers.get("Authorization").split(" ")[1]

    # find the player by given access token
    try: 
        player = Player.objects.get(token=token) # get the player
    # except User.DoesNotExist:
    except:
        # player with given token not found, return error
        return Response({'error': 'Player with token not found'}, status=HTTP_400_BAD_REQUEST)

    return Response({"name": player.name})
