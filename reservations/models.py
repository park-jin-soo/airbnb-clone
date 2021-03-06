from django.db import models
from core import models as core_models
from django.utils import timezone


class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def ___str__(self):
        return f"{self.room} - {self.guest.check_in}"

    def in_progress(self):

        now = timezone.now().date()
        if now >= self.check_in and now <= self.check_out:
            return "Ongoing"
        elif now > self.check_out:
            return "Finished"
        else:
            return "Not yet"


# in_progress.boolean = True
