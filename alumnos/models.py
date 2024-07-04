from django.db import models

# Modelo para género
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

# Modelo para alumno
class Alumno(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

    class Meta:
        ordering = ['rut']

# Modelo para producto
class Producto(models.Model):
    title = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnailUrl = models.CharField(max_length=255)  # O usar ImageField si manejas imágenes
    cantidad = models.IntegerField(default=0)  # Agregado para manejar la cantidad en stock

    def __str__(self):
        return self.title
