from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    username = None
    
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Identificador Único"
    )
    
    full_name = models.CharField(_("Nome Completo"), max_length=255)
    email = models.EmailField(_("Endereço de e-mail"), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    
    def __str__(self):
        return self.email