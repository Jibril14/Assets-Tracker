from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        STAFF = "STAFF", _('Staff')
        EMPLOYEE = "EMPLOYEE", _('Employee')

    base_role = Role.STAFF
    role = models.CharField(max_length=50, choices=Role.choices)
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name=_("Username"))
    first_name = models.CharField(max_length=150, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=150, verbose_name=_("Last Name"))
    email = models.EmailField(unique=True, verbose_name=_("Email Address"))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    company_id = models.PositiveIntegerField(null=True, blank=True)
  
    # At creation we assign a base role, at updating still maintain this role
    def save(self, *args, **kwargs):
        if not self.pk:  
            self.role = self.base_role
            return super().save(*args, **kwargs)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"


class StaffManager(CustomUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.STAFF)


class Staff(User):
    base_role = User.Role.STAFF
    staff = StaffManager()

    class Meta:
        proxy = True

    def welcome(slef):
        return "Staff User"


class EmployeeManager(CustomUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.EMPLOYEE)


class Employee(User):
    base_role = User.Role.EMPLOYEE
    employee = EmployeeManager()

    class Meta:
        proxy = True

    def welcome(slef):
        return "Employee User"
