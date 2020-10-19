from django.shortcuts import render
from .models import Item

# Create your views here.
def index(request):

  # TODO improve this when I have time
  item1 = Item()
  item1.name = "Proin vel ligula"
  item1.image = "item-01.jpg"
  item1.price = 15.00
  item1.sale = True
  
  item2 = Item()
  item2.name = "Erat odio rhoncus"
  item2.image = "item-02.jpg"
  item2.price = 25.00
  item2.sale = True

  item3 = Item()
  item3.name = "Integer vel turpis"
  item3.image = "item-03.jpg"
  item3.price = 35.00
  item3.sale = False

  item4 = Item()
  item4.name = "Sed purus quam"
  item4.image = "item-04.jpg"
  item4.price = 45.00
  item4.sale = True

  item5 = Item()
  item5.name = "Morbi aliquet"
  item5.image = "item-05.jpg"
  item5.price = 55.00
  item5.sale = True

  item6 = Item()
  item6.name = "Urna ac diam"
  item6.image = "item-06.jpg"
  item6.price = 65.00
  item6.sale = False

  item7 = Item()
  item7.name = "Proin eget imperdiet"
  item7.image = "item-04.jpg"
  item7.price = 75.00
  item7.sale = True

  item8 = Item()
  item8.name = "Nullam risus nisl"
  item8.image = "item-05.jpg"
  item8.price = 85.00
  item8.sale = False

  item9 = Item()
  item9.name = "Cras tempus"
  item9.image = "item-06.jpg"
  item9.price = 95.00
  item9.sale = False

  items = [item1, item2, item3, item4, item5, item6, item7, item8, item9]

  return render(request, 'index.html', {'items': items})