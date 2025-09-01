from django.contrib import admin

# Register your models here.

from .models import Contact  # Make sure the model name matches





class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # ✅ Valid fields

admin.site.register(Contact, ContactAdmin)



from .models import TripBooking  # replace with your model name

admin.site.register(TripBooking)

