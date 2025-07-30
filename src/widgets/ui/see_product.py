from django_components import component

@component.register('see_product')
class SeeProduct(component.Component):
    template_name = 'ui/see_product.html'
