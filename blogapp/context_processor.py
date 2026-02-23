from blogapp.models import Category, Social


def get_category(request):
    categories = Category.objects.all()
    return dict(categories = categories)


def social_links(request):
    social_links = Social.objects.all()
    return dict(social_links = social_links)