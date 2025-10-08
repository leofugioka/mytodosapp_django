from django.db import models
from django.conf import settings
import uuid

# Create your models here.

class TaskList(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='task_lists',
        verbose_name="Usuário"
    )
    name = models.CharField(max_length=255, verbose_name="Nome da Lista")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado em")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Lista de Tarefas"
        verbose_name_plural = "Listas de Tarefas"