from django.shortcuts import render
from .models import Alumno, Producto

def index(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos": alumnos}
    return render(request, 'alumnos/index.html', context)

def listadoSQL(request):
    alumnos = Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    context = {"alumnos": alumnos}
    return render(request, 'alumnos/listadoSQL.html', context)

def carrito(request):
    carrito = {
        1: {'id': 1, 'title': 'Camiseta 1', 'precio': 15000, 'cantidad': 2, 'talla': 'M'},
        2: {'id': 2, 'title': 'Camiseta 2', 'precio': 20000, 'cantidad': 1, 'talla': 'S'},
        3: {'id': 3, 'title': 'Camiseta 3', 'precio': 25000, 'cantidad': 3, 'talla': 'L'},
    }
    
    total_precio = sum(item['cantidad'] * item['precio'] for item in carrito.values())
    total_cantidad = sum(item['cantidad'] for item in carrito.values())
    
    context = {
        'carrito': carrito.values(),
        'productos': Producto.objects.all(),
        'total_precio': total_precio,
        'total_cantidad': total_cantidad,
    }
    
    return render(request, 'alumnos/carrito.html', context)

def productos(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'alumnos/Productos.html', context)

def descpolera1(request):
    descpolera1 = Producto.objects.all()
    context = {"descpolera1": descpolera1}
    return render(request, 'alumnos/descpolera1.html', context)

def descpolera2(request):
    descpolera2 = Producto.objects.all()
    context = {"descpolera2": descpolera2}
    return render(request, 'alumnos/descpolera2.html', context)

def descpolera3(request):
    descpolera3 = Producto.objects.all()
    context = {"descpolera3": descpolera3}
    return render(request, 'alumnos/descpolera3.html', context)

def descpolera4(request):
    descpolera4 = Producto.objects.all()
    context = {"descpolera4": descpolera4}
    return render(request, 'alumnos/descpolera4.html', context)

def descpolera5(request):
    descpolera5 = Producto.objects.all()
    context = {"descpolera5": descpolera5}
    return render(request, 'alumnos/descpolera5.html', context)

def quienes_somos(request):
    quienes_somos = Alumno.objects.all()
    context = {"quienes_somos": quienes_somos}
    return render(request, 'alumnos/quienes_somos.html', context)

def envios(request):
    envios = Alumno.objects.all()
    context = {"envios": envios}
    return render(request, 'alumnos/envios.html', context)

def devolucion(request):
    devolucion = Alumno.objects.all()
    context = {"devolucion": devolucion}
    return render(request, 'alumnos/devolucion.html', context)

def pago(request):
    pago = Alumno.objects.all()
    context = {"pago": pago}
    return render(request, 'alumnos/pago.html', context)
