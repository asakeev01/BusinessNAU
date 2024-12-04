from django import forms
from django.contrib import admin
from .models import StaffMember

class StaffMemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_order = StaffMember.objects.count() + 1  # Calculate dynamic range
        self.fields['order'].widget = forms.Select(
            choices=[(i, str(i)) for i in range(1, max_order + 1)]
        )

    class Meta:
        model = StaffMember
        fields = '__all__'


@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    form = StaffMemberForm
    list_display = ('name', 'position', 'email', 'order')  # Display order
    list_editable = ('order',)  # Allow inline editing of the order field
    ordering = ('order',)
