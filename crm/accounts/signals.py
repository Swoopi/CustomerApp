from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Customer

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer') # This is a form, not a formset
        instance.groups.add(group) # This is a form, not a formset
        Customer.objects.create(
            user=instance,
            name=instance.username,

        )
        print('Profile created!')

post_save.connect(customer_profile, sender=User) # This is a form, not a formset