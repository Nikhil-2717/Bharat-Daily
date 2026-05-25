from blog.models import Category, SocialLink


def get_categories(request):
      categories = Category.objects.all()
      return dict(categories=categories)

def get_social_link(request):
      social_link = SocialLink.objects.all()
      return dict(social_link=social_link)