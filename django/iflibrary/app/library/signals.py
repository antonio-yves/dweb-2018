from django.db.models.signals import pre_save, post_save

from . import models

# Reservation - Pre-save
def reservation_pre_save(sender, instance, **kwargs):
  if instance.book.available == 0:
    raise Exception('Book is unavailable')

pre_save.connect(reservation_pre_save, sender=models.Reservation)

# Reservation - Post-save
def reservation_post_save(sender, instance, created, **kwargs):
  if created:
    instance.book.available -= 1
    instance.book.save()

post_save.connect(reservation_post_save, sender=models.Reservation)