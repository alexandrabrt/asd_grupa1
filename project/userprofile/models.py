from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):

    location = models.ForeignKey('aplicatie1.Location', on_delete=models.CASCADE, null=True)
