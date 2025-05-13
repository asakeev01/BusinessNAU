from django.db import models

from solo.models import SingletonModel


class StaffPageConfig(SingletonModel):
    name = models.CharField(max_length=255)
    header_image = models.ImageField()
    main_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "Site Configuration"


class StaffMember(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    room_number = models.CharField(max_length=50, blank=True, null=True)
    curriculum_vitae = models.FileField(upload_to='cv/', blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']

class Education(models.Model):
    DEGREE_CHOICES = [
        ('PhD', 'Ph.D'),
        ('MS', 'M.S.'),
        ('BS', 'B.S.'),
        ('BA', 'B.A.'),
        ('MBA', 'M.B.A.'),
        ('MA', 'M.A.'),
        ('MD', 'M.D.'),
        ('JD', 'J.D.'),
        ('DVM', 'D.V.M.'),
    ]

    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=10, choices=DEGREE_CHOICES)
    institution = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.get_degree_display()} - {self.institution}"
