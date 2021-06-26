from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db import models
# Register your models here.
from .models import Product,ProductInCart,Cart,Order,Deal
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','is_staff','is_active')
    list_filter = ('email','is_staff','is_active')
    fieldsets = (
            (None,{'fields':('email','password')}),
            ('Permissions',{'fields':('is_active','is_staff')})
    )
    add_fieldsets = (
        (None,{'classes':('wide',),'fields':('email','password1','password2','is_staff','is_active','is_superuser')}),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser,CustomUserAdmin)



class ProductInCartInline(admin.TabularInline):
    model= ProductInCart


class CartInline(admin.TabularInline):
    model = Cart


class DealInline(admin.TabularInline):
    model = Deal.user.through


# class UserAdmin(UserAdmin):
#     model = User
#     list_display = ['username','get_cart','is_staff','is_active']
#     list_filter = ['username','is_staff','is_active']
#     fieldsets = (
#         (None,{'fields':('username','password')}),
#         ('Permissions',{'fields':('is_staff',('is_active','is_superuser'),)}),
#         ('Advanced options',{'classes':('collapse',),'fields':('groups','user_permissions')}),
#     )

#     add_fieldsets = (
#         (None,{'classes':('wide',),'fields':('username','password1','password2','is_staff','is_active','is_superuser','groups')}),
#     )
#     inlines = [
#         CartInline,DealInline
#     ]

#     def get_cart(self,obj):
#         return obj.cart
    
#     search_fields = ('username',)
#     ordering = ('username',)

# admin.site.unregister(User)

# admin.site.register(User,UserAdmin)


admin.site.register(Product)
admin.site.register(ProductInCart)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Deal)