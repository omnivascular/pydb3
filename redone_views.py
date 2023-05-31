
from django.db.models import Q

def search_products(request):
	if request.method == "POST":
		searched = request.POST['searched']
		products = Product.objects.filter(Q(name__contains=searched) | Q(vendor_id=searched) | Q(size=searched))

		return render(request, 'pydbapp/search_products.html', {'searched': searched, 'products': products})
	else:
		return render(request, 'pydbapp/search_products.html', {})


def search_vendors(request):
	if request.method == "POST":
		searched = request.POST['searched']
		vendors = Vendor.objects.filter(Q(name__contains=searched) | Q(id=searched))

		return render(request, 'pydbapp/search_vendors.html', {'searched': searched, 'vendors': vendors})
	else:
		return render(request, 'pydbapp/search_vendors.html', {})

def all_vendors(request):
	vendors = Vendor.objects.all()
	num_vendors = Vendor.objects.count()
	return render(request, 'pydbapp/show_vendors.html', {'vendors': vendors, 'num_vendors': num_vendors})

def all_products(request):
	products = Product.objects.all()
	num_products = Product.objects.count()
	return render(request, 'pydbapp/show_products.html', {'products': products, 'num_products': num_products})

def show_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	return render(request, 'pydbapp/show_product.html', {"product": product})


# re-done urls.py (for pydbapp dir)

urlpatterns = [
	path('search_products/', views.search_products, name="search_products"),
	path('search_vendors/', )
]