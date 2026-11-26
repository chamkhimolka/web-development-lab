from django.db import models


class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "En attente"
        CONFIRMED = "confirmed", "Confirmé"
        CANCELED = "canceled", "Annulé"

    # ... tes autres champs ...

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,

    )
    doctor = models.ForeignKey('AccountApp.Doctor', on_delete=models.CASCADE, null=True, blank=True)
