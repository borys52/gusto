from django.contrib import admin
from .models import Category
from .models import Dish
from .models import History
from .models import Chef
from .models import Phone
from .models import Adress
from .models import OpeningHours
from .models import CafeInfo
from .models import Message


# Register your models here.
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(History)
admin.site.register(Chef)
admin.site.register(Phone)
admin.site.register(Adress)
admin.site.register(OpeningHours)
admin.site.register(CafeInfo)
admin.site.register(Message)