from django_components import Component, register

@register("navbar")
class Navbar(Component):
    template_file = "components/navbar.html"