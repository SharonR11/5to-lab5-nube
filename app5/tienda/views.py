from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .models import Alumno
from django.db.models import Q

def inicio(request):
    alumno_list=Alumno.objects.all()
    context={"alumno_list":alumno_list}
    return render(request,'contactos.html',context)

# def menu(request): 
#     alumno_list=Alumno.objects.all()
#     context={"alumno_list":alumno_list}
#     return render(request, 'contactos.html',context)

def registraralumno(request):
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    email=request.POST["txtemail"]
    celular=request.POST["txtcelular"] 
    fecha_nac=request.POST["txtfecha"]
       
    alumno=Alumno.objects.create(nombre=nombre,apellido=apellido,email=email,celular=celular,fecha_nac=fecha_nac)
    return redirect('/')

#Editar Contacto
def editar(request,idAlumno):
    alumno=get_object_or_404(Alumno,idAlumno=idAlumno)

    if request.method == 'POST':
        nombre = request.POST.get('txtnombre')
        apellido = request.POST.get('txtapellido')
        email = request.POST.get('txtemail')
        celular = request.POST.get('txtcelular')
        fecha_nac = request.POST.get('txtfecha')

        alumno.nombre = nombre
        alumno.apellido = apellido
        alumno.email = email
        alumno.celular = celular
        alumno.fecha_nac = fecha_nac

        # Guardar los cambios en la venta
        alumno.save()

        # Redireccionar a una página de éxito o a la página de detalles de la venta
        return redirect('/')
    return render(request, 'contactos.html', {'alumno': alumno})

#Eliminar Contacto
def eliminar(request, idAlumno):

    alumno = Alumno.objects.get(idAlumno=idAlumno)
    alumno.delete()
    return redirect('/')
