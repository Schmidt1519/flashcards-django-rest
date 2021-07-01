from django.contrib import admin
from .models import Collection
from .models import Card

# Register your models here.
admin.site.register(Collection)
admin.site.register(Card)