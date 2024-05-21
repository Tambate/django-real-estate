from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
# ho tro da ngon ngu
from django.utils.translation import gettext_lazy as _


class CustomerUserManager(BaseUserManager):

    def emai_validator(self, email):
        try:
            validate_email(email)
        except:
            raise ValidationError(_("You must provide a valid email address"))

    def create_user(self, username, first_name, last_name, email, password, **extra_fields):

        if not username:
            raise ValidationError(_("Users must submit username"))

        if not first_name:
            raise ValidationError(_("Users must submit firstname"))

        if not last_name:
            raise ValidationError(_("Users must submit lastname"))

        if email:
            email = self.normalize_email(email)
            self.emai_validator(email)
        else:
            raise ValidationError(_("Base User Account: An Email Address is required"))

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, password, email, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValidationError(_("Superuser is must have is_staff=True"))
        
        
        if extra_fields.get("is_superuser") is not True:
            raise ValidationError(_("Superuser is must have is_superuser=True"))
        
        if not password:
            raise ValidationError(_("Superuser must have a password"))
        
        if email:
            email = self.normalize_email(email)
            self.emai_validator(email)

        else:
            raise validate_email(_("Admin Account: An Email Address is required"))
        
        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user

