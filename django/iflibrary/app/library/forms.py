from django import forms

from . import models

# Reservation
class ReservationForm(forms.ModelForm):

  # status = forms.ChoiceField(widget=forms.RadioSelect, choices=models.Reservation.STATUS)
  
  class Meta:
    model = models.Reservation
    fields = ('book', 'status', 'updated_date')#('__all__')
    widgets = {
      'status': forms.RadioSelect(choices=models.Reservation.STATUS)
    }

# Reservation
class BookReservationForm(forms.ModelForm):

  book = forms.IntegerField(widget=forms.HiddenInput())
  status = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
  
  class Meta:
    model = models.Reservation
    fields = ('book', 'status')#('__all__')
    # widgets = {
    #   'status': forms.RadioSelect(choices=models.Reservation.STATUS)
    # }