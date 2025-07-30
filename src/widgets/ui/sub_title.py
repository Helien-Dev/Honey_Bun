from django_components import component

@component.register("sub_title")
class SubTile(component.Component):
    template_name = "ui/sub_title.html"
    # class Media:
    #     css = 'Sub_Title/style.css'
    #     js = 'Sub_Ttile'