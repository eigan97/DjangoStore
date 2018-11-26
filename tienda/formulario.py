from django import forms  #incorpora los formualrios de django
from tienda.models import producto,categoriaProducto

class ProductoForm(forms.ModelForm):
	class Meta: 
		model = producto 

		fields= [ 
		'nombre' ,
		'descripcion',
		'precio' ,		
		'stock',
		'categorias',
		'status'

		]
		# placeholder={
		# 'nombre' : 'Nombre',
		# 'descripcion': 'Descripcion del Producto',
		# 'costo' : 'Costo',
		# 'disponible': 'Disponible',
		# 'numeroExistencias': 'Numero de Existencias',
		# 'categoria': 'Categoria',

		# }
		widget={
		'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
		'descripcion':forms.TextInput(),
		'precio' : forms.FloatField(),
		'status': forms.widgets.CheckboxInput(),
		'stock': forms.IntegerField(),
		'categorias': forms.ModelChoiceField(queryset=categoriaProducto.objects.all()),

		}

class CategoriaForm(forms.ModelForm):
	class Meta: 
		model = categoriaProducto 

		fields= [ 
		'nombre' ,
		'descripcion',
		

		]
		labels={
		'nombre' : 'Nombre',
		'descripcion': 'Descripcion',
		

		}

		
		widget={
		'nombre' : forms.TextInput(),
		'descripcion' : forms.TextInput(),

		

		}

		