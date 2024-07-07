from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    # email and username are passed here because these are required to create Account
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username address")
        
        user = self.model(
            email=self.normalize_email(email),  #normalize converts email to lowercase
            username=username, 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(
            email,
            password=password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    #required for custom model
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    data_joined = models.DateTimeField(verbose_name= 'date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name= 'last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    #not required
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(default='profile_pictures/default_profile_img.jpg', null=True, blank=True, upload_to='profile_pictures/')

    objects = MyAccountManager()

    #what to log in with and what is required while registering
    USERNAME_FIELD = 'email'
    #what is required while registering in addition to the above
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True