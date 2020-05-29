"""ElCentro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from administracion.views import inicio, logout, InfromeDeInvetario, informes
from ventas.views import InfromeDeVenta, InfromeDeVentaCoDet
from devoluciones.views import InfromeDeInvetarioDef
from compras.views import InfromeDeCompra, InfromeDeCompraCoDet

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', inicio), 
	path('logout', logout),
	path('informes', informes),
    path('admin/', admin.site.urls),
    path('venta', InfromeDeVenta.as_view(), name= 'mi_pdf'),
    path('ventadet', InfromeDeVentaCoDet.as_view(), name= 'venta_det'),
    path('compra', InfromeDeCompra.as_view(), name= 'mi_pdf'),
    path('compradet', InfromeDeCompraCoDet.as_view(), name= 'venta_det'),
    path('inventario', InfromeDeInvetario.as_view(), name= 'inventario'),
    path('inventariodef', InfromeDeInvetarioDef.as_view(), name= 'informe_dev'),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

