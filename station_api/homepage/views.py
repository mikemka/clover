import django.shortcuts


def homepage(request):
    template_name = 'homepage/homepage.html'
    return django.shortcuts.render(
        request=request,
        template_name=template_name,
    )