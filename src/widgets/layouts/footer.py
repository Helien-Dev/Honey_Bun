from django_components import Component, register

@register("footer")
class Footer(Component):
    template_file = "components/layouts/footer.html"