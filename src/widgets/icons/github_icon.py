from django_components import Component, register

@register("github_icon")
class GithubIcon(Component):
    template_name = "components/icons/github_icon.html"
