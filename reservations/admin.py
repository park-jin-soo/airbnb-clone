from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Reservation Models Definition"""

    list_display = ("room", "status", "check_in", "check_out", "guest", "in_progress")
    # list_filter = ("status", "in_progress")
