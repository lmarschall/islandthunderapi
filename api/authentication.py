from rest_framework.authentication import TokenAuthentication
# from .models import MyOwnToken, Player

# class MyOwnTokenAuthentication(TokenAuthentication):
#     # model = MyOwnToken
#     def authenticate(self, request):

#         # get the uid of the player
#         uid = request.GET["uid"]
#         print("UID")
#         print(uid)

#         if not uid: # no username passed in request headers
#             return None # authentication did not succeed

#         try:
#             player = Player.objects.get(uid=uid) # get the player
#         # except User.DoesNotExist:
#         except:
#             return None # player not found, create new player

#         print("PLAYER")
#         print(player)

#         # return (player, None) # authentication successful
#         return (player, None)