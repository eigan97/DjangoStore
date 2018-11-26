from django.shortcuts import render, redirect,get_object_or_404
from tienda.models import producto,categoriaProducto
from django.http import HttpResponse
from tienda.formulario import ProductoForm,CategoriaForm

# Create your views here.
def index(request):
	return render(request, 'views/home.html')
def venta(request):
	return render(request, 'views/venta.html')
def all_products(request):
	cntx = { 
		'productos': producto.objects.all()
	}
	return render(request, 'views/listproducts.html',cntx)

def all_productsA(request):
	cntx = { 
		'productos': producto.objects.all()
	}
	return render(request, 'views/aproducts.html',cntx)

def all_categoriaA(request):
	cntx = { 
		'categorias': categoriaProducto.objects.all()
	}
	return render(request, 'views/acategorias.html',cntx)

def add_product_submit(request):
	if request.method == 'POST':
		form=ProductoForm(request.POST)
		if form.is_valid(): 
			form.save() 
		return redirect('adminpPoductos')
	else: 
		form = ProductoForm()
	return render(request, 'views/productosForm.html',{'form': form})

def add_categorias_submit(request):
	if request.method == 'POST':
		form=CategoriaForm(request.POST)
		if form.is_valid(): 
			form.save() 
		return redirect('adminCategorias')
	else: 
		form = CategoriaForm()
	return render(request, 'views/categoriasForm.html',{'form': form})
def add_categorias(request):
	return render(request, 'views/categoriasForm.html')
#Eliminar Editar


def eliminar_producto(request,id_producto):
	Producto=producto.objects.get(id=id_producto)
	Producto.delete()
	return redirect('adminpPoductos')

def eliminar_categoria(request,id_categoria):
	categoria=categoriaProducto.objects.get(id=id_categoria)
	categoria.delete()
	return redirect('adminCategorias')

def editar_producto(request,id_producto):
	instance = get_object_or_404(producto, id=id_producto)
	form = ProductoForm(instance=instance)
	if form.is_valid():
		form.save(commit=False)
		return redirect('adminpPoductos')
	return render(request, 'views/productosForm.html',{'form': form})

def editar_categoria(request,id_categoria):
	instance = get_object_or_404(categoriaProducto, id=id_categoria)
	form = ProductoForm(instance=instance)
	if form.is_valid():
		form.save(commit=False)
		return redirect('adminCategorias')
	return render(request, 'views/categoriasForm.html',{'form': form})