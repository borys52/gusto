from django.shortcuts import render,redirect
from .models import Category, Dish, History, Chef,Phone, Adress, OpeningHours, CafeInfo, Message
from .forms import FormMessage

# Create your views here.
def main_page_view(request):
    if request.method == "POST":
        form = FormMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    for item in categories:
        dishes = Dish.objects.filter(category=item.pk).filter(is_visible=True).order_by('dish_order')
        item.dishes = dishes


    special = Dish.objects.filter(category__title='Специальное Меню')
    history = History.objects.all()
    chef = Chef.objects.all().filter(is_visible=True)
    phone = Phone.objects.all()
    adress = Adress.objects.all()
    openhour = OpeningHours.objects.all()
    cafeinfo = CafeInfo.objects.all()
    message = Message.objects.all()
    form = FormMessage()

    return render(request, 'index.html', context={
        'categories': categories,
        'special': special,
        'history': history[0],
        'chef': chef[0],
        'phone': phone[0],
        'adress': adress[1],
        'openhour': openhour[0],
        'cafeinfo': cafeinfo[0],
        'message': message,
        'form': form
    })

def dish_page_view(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'dish_info.html' , context={'dish': dish})