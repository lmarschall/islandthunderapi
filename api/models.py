import binascii
import os

from django.db import models
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _

class Player(models.Model):

    name = models.CharField(max_length=50, default="")
    uid = models.CharField(max_length=64, default="")
    token = models.CharField(max_length=40, default="")
    authorized = models.BooleanField(default=False)
    # # uid = models.CharField(max_length=50, default="")

    # REQUIRED_FIELDS = ['uid']
    # USERNAME_FIELD = ['name']

    # is_active = False
    # set_password = None
    # is_anonymous = False
    # is_authenticated = False

    # objects = UserManager()

    # description = models.TextField()
    # latitude = models.FloatField()
    # longitude = models.FloatField()

    class Meta:
        db_table = 'api_players'
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    # def __str__(self):
    #     return "Produkt %d" % (self.nummer)

# class MyOwnToken(models.Model):
#     """
#     The default authorization token model.
#     """
#     key = models.CharField(_("Key"), max_length=40, primary_key=True)

#     player = models.ForeignKey(Player, on_delete=models.CASCADE, default=1)

#     # player = models.OneToOneField(
#     #     Player, related_name='auth_token',
#     #     on_delete=models.CASCADE, verbose_name="Player"
#     # )

#     # company = models.OneToOneField(
#     #     Company, related_name='auth_token',
#     #     on_delete=models.CASCADE, verbose_name="Company"
#     # )
#     created = models.DateTimeField(_("Created"), auto_now_add=True)

#     class Meta:
#         verbose_name = _("Token")
#         verbose_name_plural = _("Tokens")

#     def save(self, *args, **kwargs):
#         if not self.key:
#             self.key = self.generate_key()
#         return super(MyOwnToken, self).save(*args, **kwargs)

#     def generate_key(self):
#         return binascii.hexlify(os.urandom(20)).decode()

#     def __str__(self):
#         return self.key
