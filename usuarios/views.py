from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def registro(request):
    if request.method == "POST":
        formulario_p = RegistroUsuarioForm(request.POST)
        if formulario_p.is_valid():
            usuario = formulario_p.save(commit=False)
            grupo_seleccionado = formulario_p.cleaned_data["tipo_usuario"]
            print("Grupo:", grupo_seleccionado)
            if grupo_seleccionado == 'admin':
                grupo = Group.objects.get(name='admin')
            elif grupo_seleccionado == 'usuario_comun':
                grupo = Group.objects.get(name='usuario_comun')
            usuario.save()
            usuario.groups.add(grupo)
            
            username = formulario_p.cleaned_data["username"]
            messages.success(request, f'Cuenta creada de forma exitosa para el usuario {username}')
            return redirect('tienda:home')
        else:
            messages.error(request, 'Hubo un error en el registro')

    formulario = RegistroUsuarioForm()
    return render(request, "usuarios/registro.html", {'formulario':formulario})