from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm


User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None,{
            'classes' : ('wide',),
            'fields' : ('username', 'email', 'password1', 'password2')
        }),
    )
    list_display = ('email','first_name', 'last_name','surname','is_staff','email_verify', 'coins', 'affair', 'idLeadFromBitrix24')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('first_name','last_name',
                                    'surname',
                                    'phone',
                                    'email_verify',
                                    'coins',
                                    'affair',
                                    'idLeadFromBitrix24'
)}),
    )
