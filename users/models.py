from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from PIL import Image
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned

# Implement differentiation between PatientProfile and MedicalDoctorProfile
class PatientProfile(models.Model):
    #inherites from default Django User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_of_birth = models.DateTimeField(default=timezone.now)
    phone = models.CharField(blank=True, max_length=25)



    #add adress information here

    def __str__(self):
        return f'{self.user.username} Profile'

# class MedicalDoctorProfile(models.Model)

# Customized authentication Backend for Login w. email and username
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try: #to allow authentication through phone number or any other field, modify the below statement
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None
