from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import QuerySet
from django.views.generic import ListView
from .models import Product, Vendor
from django.urls import reverse
from .forms import DisplayForm

# Create your views here.

from django.db.models import Q


def search_products(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        products = Product.objects.filter(
            Q(name__contains=searched) | Q(vendor_id=searched)
        )

        return render(
            request,
            "pydbapp/search_products.html",
            {"searched": searched, "products": products},
        )
    else:
        return render(request, "pydbapp/search_products.html", {})


# def search_vendors(request):
#     if request.method == "POST":
#         searched = request.POST["searched"]
#         vendors = Vendor.objects.filter(Q(name__contains=searched) | Q(id=searched))

#         return render(
#             request,
#             "pydbapp/search_vendors.html",
#             {"searched": searched, "vendors": vendors},
#         )
#     else:
#         return render(request, "pydbapp/search_vendors.html", {})


# def show_vendors(request):
#     vendors = Vendor.objects.all()
#     num_vendors = Vendor.objects.count()
#     return render(
#         request,
#         "pydbapp/show_vendors.html",
#         {"vendors": vendors, "num_vendors": num_vendors},
#     )


# def show_products(request):
#     products = Product.objects.all()
#     num_products = Product.objects.count()
#     return render(
#         request,
#         "pydbapp/show_products.html",
#         {"products": products, "num_products": num_products},
#     )


# previous views below, trying pure function based approach above


def home(request):
    products = Product.objects.all()
    return render(request, "pydbapp/base.html", {"products": products})


def search_product(request, pk):
    product_instance = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = DisplayForm(request.POST)
        if form.is_valid():
            product_instance.quantity_on_hand = form.cleaned_data["quantity_changed"]
            product_instance.save()
            return HttpResponseRedirect(reverse("pydbapp:products"))
    else:
        basic_info = product_instance.name
        form = DisplayForm({"Current non-updated value": basic_info})
    context = {
        "form": form,
        "product_instance": product_instance,
    }

    return render(request, "pydbapp/product_search_update.html", context)


class IndexView(ListView):
    template_name = "pydbapp/index.html"

    # need to fix redudancy below
    def get_queryset(self):
        """
        Return the queryset for the view.
        """
        num_products = Product.objects.count()
        num_vendors = Vendor.objects.count()
        num_visits = self.request.session.get("num_visits", 0)
        # self.request.session["num_visits"] = num_visits + 1

        context = {
            "num_products": num_products,
            "num_vendors": num_vendors,
            "num_visits": num_visits,
        }

        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num_products = Product.objects.count()
        num_vendors = Vendor.objects.count()
        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1

        context["num_products"] = num_products
        context["num_vendors"] = num_vendors
        context["num_visits"] = num_visits

        return context

    # def dispatch(self, request, *args, **kwargs):
    #     self.request = request
    #     return super().dispatch(request, *args, **kwargs)

    # def get_queryset(self, request):
    #     """
    #     Return some info.
    #     """
    #     num_products = Product.objects.count()
    #     num_vendors = Vendor.objects.count()
    #     num_visits = self.request.session.get("num_visits", 0)
    #     self.request.session["num_visits"] = num_visits + 1

    #     context = {
    #         "num_products": num_products,
    #         "num_vendors": num_vendors,
    #         "num_visits": num_visits,
    #     }

    #     return render(request, "index.html", context=context)


# def index(request):
#     return HttpResponse("Hello World!")


class ProductHomeView(ListView):
    template_name = "pydbapp/products.html"
    model = Product

    context_object_name = "products_list"

    def get_queryset(self):
        """
        Return some info.
        """
        return Product.objects.all()


class VendorHomeView(ListView):
    template_name = "pydbapp/vendors.html"
    model = Vendor
    context_object_name = "vendors_list"

    def get_queryset(self):
        """
        Return some info.
        """
        return Vendor.objects.all()
