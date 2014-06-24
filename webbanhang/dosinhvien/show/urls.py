__author__ = 'PhamVanDan'


from django.conf.urls import  patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^all/$', 'show.views.show_products'),
    url(r'^laptop/$', 'show.views.show_products_laptop'),
    url(r'^dienthoai/$', 'show.views.show_products_dienthoai'),
    url(r'^phukien/$', 'show.views.show_products_phukien'),
    url(r'^sach/$', 'show.views.show_products_sach'),
    url(r'^banghe/$', 'show.views.show_products_banghe'),
    url(r'^khac/$', 'show.views.show_products_khac'),
    url(r'^get/(?P<product_id>\d+)/$', 'show.views.show_product'),
)