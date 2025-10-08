from django.db import models

# Create your models here.

class Task(models.Model):
    task_list = models.ForeignKey(
        'lists.TaskList',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name="Lista de Tarefas"
    )
    
    title = models.CharField(max_length=255, verbose_name="Título")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    is_completed = models.BooleanField(default=False, verbose_name="Concluído")
    due_date = models.DateTimeField(auto_now=False, blank=True, null=True, verbose_name="Finalizar até")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['is_completed', '-created_at']
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"