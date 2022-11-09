from django.contrib import admin

from products.models import ProductCategory,Product,Basket

admin.site.register(ProductCategory)
admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity','category')
    fields = ('name','image','description','short_description',('price','quantity'),'category')
    ordering = ('name',)
    search_fields = ('name',)


class BasketInline(admin.TabularInline):
    model = Basket
    fields = ('product','quantity','created_timestamp')
    readonly_fields = ('created_timestamp',)