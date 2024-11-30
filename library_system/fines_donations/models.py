from django.db import models
from django.contrib.auth.models import User

# Fines model to track user fines
class Fine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    paid = models.BooleanField(default=False)
    date_issued = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.amount}"

# Donations model to track user donations
class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(null=True, blank=True)
    date_donated = models.DateField(auto_now_add=True)

    def clean(self):
        if self.amount <= 0:
            raise ValidationError("Donation amount must be greater than zero.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Donation from {self.user.username} - {self.amount}"




