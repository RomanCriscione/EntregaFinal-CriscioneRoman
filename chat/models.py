from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    asunto = models.CharField(max_length=255)  # <-- AGREGAMOS ESTA LÍNEA
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Asunto: {self.asunto} | De {self.remitente} para {self.destinatario} - {self.fecha_envio}'
