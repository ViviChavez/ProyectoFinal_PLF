from django.contrib import admin

# Register your models here.
from libro.models import *


admin.site.register(Libro)
admin.site.register(Cliente)
admin.site.register(Ventas)
