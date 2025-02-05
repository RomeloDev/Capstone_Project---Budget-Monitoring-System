from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, department=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not username:
            raise ValueError("Users must have a username")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, department=department)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        """Creates and returns a superuser."""
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
# Custom User Model
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, max_length=255)
    department = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Django authentication fields
    is_active = models.BooleanField(default=True)  # Required for login
    is_staff = models.BooleanField(default=False)  # Required for Django admin
    is_superuser = models.BooleanField(default=False)  # Superuser flag
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'  # This field is used for authentication
    REQUIRED_FIELDS = ['email']  # These fields are required when using createsuperuser
    
    def __str__(self):
        return self.username