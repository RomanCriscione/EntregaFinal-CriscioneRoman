from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm

# Bandeja de entrada
@login_required
def inbox(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    return render(request, 'chat/inbox.html', {'mensajes': mensajes_recibidos})

# Enviar un mensaje
@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('inbox')
    else:
        form = MensajeForm()
    return render(request, 'chat/enviar_mensaje.html', {'form': form})
