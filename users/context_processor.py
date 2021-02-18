from .form import FormNavBar

################################################################################

def form_renderer(request):
    """
    We create by ourselves this function which will returns this form as a
    context_processor because this form is on base.html
    """
    return {'form_nav_bar' : FormNavBar()}