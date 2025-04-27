from django.contrib import admin
from .models import Mensaje

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('remitente', 'destinatario', 'asunto', 'fecha_envio')
    search_fields = ('remitente__username', 'destinatario__username', 'asunto')
