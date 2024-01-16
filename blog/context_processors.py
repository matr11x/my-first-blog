from .models import Category

def common_context(request):
    cat_menu = Category.objects.all()
    return {'cat_menu': cat_menu}