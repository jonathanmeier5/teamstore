from django.template.response import TemplateResponse

from ..dashboard.views import staff_member_required
from ..product.utils import products_with_availability, products_for_homepage
from ..teamstore.utils import get_team

def home(request,**kwargs):

    team = get_team(request.session['team'])
    products = products_for_homepage(team)[:8]
    products = products_with_availability(
        products, discounts=request.discounts, local_currency=request.currency)
    return TemplateResponse(
        request, 'home.html',
        {'products': products, 'parent': None})


@staff_member_required
def styleguide(request):
    return TemplateResponse(request, 'styleguide.html')
