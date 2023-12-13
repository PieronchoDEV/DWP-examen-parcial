from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto, Tienda
from django.urls import reverse

# Create your views here.
def index(request):
    if request.method=='POST':
        nuuevoDireccion=request.POST.get('nuevoDireccion')
        nuevoProvincia=request.POST.get('nuevoProvincia')
        nuevoRegion=request.POST.get('nuevoRegion')
        nuevoFecha=request.POST.get('nuevoFecha')
        nuevoTel=request.POST.get('nuevoTel')
        
        Tienda.objects.create(
            direccion=nuuevoDireccion,
            provincia=nuevoProvincia,
            region=nuevoRegion,
            fechaCreacion=nuevoFecha,
            telefonoContacto=nuevoTel
        )
        
        return HttpResponseRedirect(reverse('gestionTienda:index'))
    return render(request,'tienda.html',{
        'tiendasTotales':Tienda.objects.all()
    })

#{% url 'gestionTienda:Productos' %}
def productos(request):
    if request.method=='POST':
        nuuevoDescripcion=request.POST.get('nuevoDescripcion')
        nuevoPrecio=request.POST.get('nuevoPrecio')
        nuevoCantidad=request.POST.get('nuevoCantidad')
        nuevoProducto=Producto.objects.create(
            descripcion=nuuevoDescripcion,
            precioDeVenta=nuevoPrecio,
            cantidad=nuevoCantidad
        )
        nuevoCodigo=str(nuevoProducto.id)
        while len(nuevoCodigo)<4:
            nuevoCodigo='0'+nuevoCodigo
        nuevoCodigo='PRO-'+nuevoCodigo
        
        nuevoProducto.codigo=nuevoCodigo
        nuevoProducto.save()
        return HttpResponseRedirect(reverse('gestionTienda:productos'))
    return render(request,'productos.html',{
        'productosTotales':Producto.objects.all(),
        'tiendaTotales':Tienda.objects.all()
    })
    
def eliminarProducto(request,idProducto):
    objProducto=Producto.objects.get(id=idProducto)
    objProducto.delete()
    return HttpResponseRedirect(reverse('gestionTienda:productos'))

def eliminarTienda(request,idTienda):
    objTienda=Tienda.objects.get(id=idTienda)
    objTienda.delete()
    return HttpResponseRedirect(reverse('gestionTienda:index'))

def asignarTienda(request):
    if request.method=='POST':
        idProducto=request.POST.get('productoSeleccionado')
        idTienda=request.POST.get('tiendaSeleccionado')
        objProducto=Producto.objects.get(id=idProducto)
        objTienda=Tienda.objects.get(id=idTienda)
        objProducto.tiendaRelacionada=objTienda
        objProducto.save()
        return HttpResponseRedirect(reverse('gestionTienda:productos'))
    
def detalleTienda(request,idTienda):
    objTienda=Tienda.objects.get(id=idTienda)
    datos_Tienda=objTienda.producto_set.all()
    return render(request,'tiendaDetalles.html',{
        'objTienda':objTienda,
        'datos_Tienda':datos_Tienda
    })