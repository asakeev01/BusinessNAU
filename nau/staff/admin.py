from django.contrib import admin
from django import forms

from .models import *
from solo.admin import SingletonModelAdmin

class StaffMemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dynamically set the choices for 'order' field
        max_order = StaffMember.objects.count() + 1  # Add 1 to include the new staff member
        self.fields['order'].widget = forms.Select(
            choices=[(i, str(i)) for i in range(1, max_order + 1)]  # Generate choices from 1 to max_order
        )

    class Meta:
        model = StaffMember
        fields = '__all__'


@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    form = StaffMemberForm  # Use custom form
    list_display = ('name', 'position', 'email', 'order')  # Display 'order' field in the list view
    list_editable = ('order',)  # Allow inline editing of 'order'
    ordering = ('order',)  # Ensure the staff list is ordered by 'order'

admin.site.register(StaffPageConfig, SingletonModelAdmin)
admin.site.register(Education)